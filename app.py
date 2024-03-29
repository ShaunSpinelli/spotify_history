"""Main App"""

import os
import time
import base64
import requests
from flask import Flask, redirect, request
from flask import render_template
from flask_cors import CORS, cross_origin
import boto3
from boto3.dynamodb.conditions import Key
import dateutil
import logging
import utils
import stats

import song_stats

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")


logger = logging.getLogger(__name__)


import spotipy
from spotipy.oauth2 import SpotifyOAuth
#TODO: DO NOT COMMIT SPOTIFY ID and SECRET!!!!!!!!!
APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "")
DYNAMODB_ENDPOINT = os.environ.get("DYNAMO_ENDPOINT", "http://localhost:8888")
REDIRECT_URI = os.environ.get("REDIRECT_URI", "http://localhost:5000/registercallback")


SCOPE = "user-read-recently-played"

app = Flask(__name__, static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    logger.info(f"DYNAMODB_ENDPOINT: {DYNAMODB_ENDPOINT}")
    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT, region_name='us-west-2')
    table = dynamodb.Table('Users')
    r = table.put_item(Item={
        "id": 12334,
        "name": 'Jimbo',
        "token": '1233460bdfsg',
        "last_fetch": None
    })
    return r



@app.route('/register', methods=["POST"])
def register():
    #TODO: include state in the request

    return redirect("https://accounts.spotify.com/authorize?"
                    f"response_type=code"
                    f"&client_id={APP_CLIENT_ID}"
                    f"&scope={SCOPE}"
                    f"&redirect_uri={REDIRECT_URI}")


@app.route('/registercallback')
def register_new_user():
    # get access and refresh token
    code = request.args.get('code')
    state = request.args.get('state')

    payload = {"code": code, "redirect_uri": f"{REDIRECT_URI}", "grant_type":"authorization_code"}

    auth_str = f"{APP_CLIENT_ID}:{APP_CLIENT_SECRET}"

    password_base64 = base64.urlsafe_b64encode(auth_str.encode()).decode()

    headers = {"Authorization": f"Basic {password_base64}", 'Content-Type': 'application/x-www-form-urlencoded'}

    # TODO: handle this response better

    res = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=payload)

    logger.debug(res.status_code)


    token_data = res.json()


    logger.debug(token_data)
    if token_data.get('error'):
        return token_data

    # add extra field Spotipy is expecting
    token_data["expires_at"] = int(time.time()) + token_data["expires_in"]

    token_path = "./token_data"

    utils.save_json(token_data, token_path)

    logger.debug("Setting up spotipy Oauth")
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        cache_path=token_path,
                        redirect_uri=REDIRECT_URI)
    sp = spotipy.Spotify(auth_manager=auth)

    user = sp.current_user()
    token = auth.get_cached_token()

    new_user = { "id": user["id"],
                 "name": user["display_name"],
                 "token": token,
                 "last_fetch": None}

    logger.warning("Adding user to db")

    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT, region_name='us-west-2')
    table = dynamodb.Table('Users')

    # check if user is registered, if they are redirect them to their songs page
    response = table.get_item(Key={
        "id": user["id"],
        "name": user["display_name"],
    })

    if response.get("Item") is not None:
        logger.warning(f"Updating user: {user['display_name']} with new token")
        response2 = table.update_item(
            Key={
                "id":user["id"],
                "name": user["display_name"]
            },
            UpdateExpression="set #tok=:t",
            ExpressionAttributeValues={
                ':t': token,
            },
            ExpressionAttributeNames={
                "#tok": "token"
            }
        )
        os.remove(token_path)
        return redirect(f"mysongs/{user['id']}")

    # add user to db
    r = table.put_item(Item=new_user)

    # delete tmp .cache
    os.remove(token_path)

    return render_template("successful.html",
                           name=new_user["name"],
                           id=new_user["id"],)



@app.route('/mysongs/table/<user_id>')
def get_users_songs_table(user_id):
    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)

    try:
        table = dynamodb.Table('Songs')
        history = table.query(
        KeyConditionExpression=Key('user').eq(user_id)
    )
    except FileNotFoundError:
        return "User Does Not Exist"

    for song in history["Items"]:
        t = dateutil.parser.parse(song["played_at"])
        song["unix_time"] = t.timestamp()
        song["played_at"] = t.strftime("%c")

    history["Items"].sort(key= lambda x: x.get("unix_time"), reverse=True)

    return render_template("songs.html", songs=history["Items"])


# API STUFF
@app.route('/api/user/<user_id>/artists')
def get_users_top_played_artists(user_id):
    artist_count = int(request.args.get('artist_count', 10))
    time_range = request.args.get('range', '1M')
    logger.info(f"artis_count: {artist_count}, time_range:{time_range}, user_id: {user_id}")

    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)

    try:
        table = dynamodb.Table('Songs')
        history = table.query(
        KeyConditionExpression=Key('user').eq(user_id)
    )
    except FileNotFoundError:
        return "User Does Not Exist"

    for song in history["Items"]:
        t = dateutil.parser.parse(song["played_at"])
        song["unix_time"] = t.timestamp()
        song["played_at"] = t.strftime("%c")

    logger.info("processing songs")
    songs_df = stats.preprocess_songs(history["Items"])
    res = stats.artist_listen_count_over_time(songs_df, time_range, artist_count)
    return res

@app.route('/api/user/<user_id>/listening')
def get_time_of_day_listening(user_id):
    time_range = request.args.get('range', 'weekday')

    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)

    try:
        table = dynamodb.Table('Songs')
        history = table.query(
        KeyConditionExpression=Key('user').eq(user_id)
    )
    except FileNotFoundError:
        return "User Does Not Exist"

    for song in history["Items"]:
        t = dateutil.parser.parse(song["played_at"])
        song["unix_time"] = t.timestamp()
        song["played_at"] = t.strftime("%c")

    logger.info("processing songs")
    songs_df = stats.preprocess_songs(history["Items"])
    res = stats.hour_of_day_listen_times_array(songs_df, time_range)
    return {"result": res}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
