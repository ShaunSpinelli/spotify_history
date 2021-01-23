"""Auth flow"""

import os
from flask import Flask
from flask import render_template
import boto3
from boto3.dynamodb.conditions import Key



import spotipy
from spotipy.oauth2 import SpotifyOAuth

APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
DYNAMODB_ENDPOINT = os.environ.get("DYNAMO_ENDPOINT")#"http://localhost:5000"
# DYNAMODB_ENDPOINT = "http://localhost:5000"


SCOPE = "user-read-recently-played"

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    print("Giving home screen")
    return render_template('index.html')

@app.route('/new_user', methods=["POST"])
def register_new_user():
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        redirect_uri="http://localhost:8888/callback")

    sp = spotipy.Spotify(auth_manager=auth)
    user = sp.current_user()
    print("Got user")
    token = auth.get_cached_token()

    new_user = { "id": user["id"],
                 "name": user["display_name"],
                 "token": token,
                 "last_fetch": None}


    print("Adding user to db")
    dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)
    table = dynamodb.Table('Users')

    response = table.put_item(Item=new_user)

    print(response)

    # first_song = fetcher.first_fetch(new_user)
    #
    # delete tmp .cache
    # os.remove(".cache")
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

        # history = table.scan()
    except FileNotFoundError:
        return "User Does Not Exist"

    return history

if __name__ == '__main__':
    app.run(host='0.0.0.0')
