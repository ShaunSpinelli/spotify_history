"""Auth flow"""

import os
from flask import Flask
from flask import render_template

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import utils
import fetcher


APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SCOPE = "user-read-recently-played"


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_user', methods=["POST"])
def register_new_user():
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        cache_path="tmp-cache",
                        redirect_uri="http://localhost:8888/callback")

    sp = spotipy.Spotify(auth_manager=auth)
    user = sp.current_user()
    new_user = utils.setup_new_user(user)

    # update users db with user
    users = utils.load_json('db/users.json')
    users["users"].append(new_user)
    utils.save_json(users,'db/users.json')

    token = auth.get_cached_token()

    utils.save_json(token, f"db/{new_user['id']}.token")

    first_song = fetcher.first_fetch(new_user)

    # NOTE: need to delete tmp
    return render_template("successful.html",
                           name=new_user["name"],
                           id=new_user["id"],
                           time=first_song["played_at"],
                           song=first_song["name"])



@app.route('/mysongs/<user_id>')
def setup_user(user_id):
    try:
        history = utils.load_json(f"db/{user_id}-history.json")
    except FileNotFoundError:
        return "User Does Not Exist"

    return history

