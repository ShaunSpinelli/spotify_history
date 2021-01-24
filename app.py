"""Main App"""

import os
import time
from flask import Flask
from flask import render_template
import boto3
from boto3.dynamodb.conditions import Key
import dateutil
import  logging

logger = logging.getLogger(__name__)



import spotipy
from spotipy.oauth2 import SpotifyOAuth

APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
DYNAMODB_ENDPOINT = os.environ.get("DYNAMO_ENDPOINT", "http://localhost:5000")
REDIRECT_URI = os.environ.get("REDIRECT_URI", "http://localhost:8000/registercallback")


SCOPE = "user-read-recently-played"

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    logger.warning("Giving home screen")
    return render_template('index.html')

@app.route('/new_user', methods=["POST"])
def register_new_user():

    logger.warning("doing some stuff")

    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        redirect_uri="http://localhost:8888/callback")
    logger.warning("Getting spotify client")
    sp = spotipy.Spotify(auth_manager=auth)
    user = sp.current_user()
    logger.warning("Got user")
    token = auth.get_cached_token()

    new_user = { "id": user["id"],
                 "name": user["display_name"],
                 "token": token,
                 "last_fetch": None}


    logger.warning("Adding user to db")
    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)
    table = dynamodb.Table('Users')

    response = table.put_item(Item=new_user)

    # delete tmp .cache
    os.remove(".cache")
    #
    return render_template("successful.html",
                           name=new_user["name"],
                           id=new_user["id"],
                           time= "123", #first_song["played_at"],
                           song="Do the harlem shake")# first_song["name"])



@app.route('/mysongs/<user_id>')
def setup_user(user_id):
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

@app.route('/registercallback')
def callback():
    return "Thanks for signing up"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
