"""Auth flow"""

import os
import time
import atexit
from flask import Flask
from flask import render_template

from apscheduler.schedulers.background import BackgroundScheduler

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import utils
import fetcher


APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SCOPE = "user-read-recently-played"

# Song history scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetcher.sync_data, trigger="interval", seconds=3 *60 * 60)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_user', methods=["POST"])
def register_new_user():
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        redirect_uri="http://localhost:8888/callback")

    sp = spotipy.Spotify(auth_manager=auth)
    user = sp.current_user()
    new_user = utils.setup_new_user(user)

    # update users db with user
    users = utils.load_json('db/users.json')
    users["users"].append(new_user)
    utils.save_json(users,'db/users.json')

    print(f"Added new user {new_user['name']}")

    token = auth.get_cached_token()

    utils.save_json(token, f"db/{new_user['id']}.token")

    first_song = fetcher.first_fetch(new_user)

    # delete tmp .cache
    os.remove(".cache")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
