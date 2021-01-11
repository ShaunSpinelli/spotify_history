import os
import time
import utils
import spotipy
from spotipy.oauth2 import SpotifyOAuth


APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SCOPE = "user-read-recently-played"


def parse_recent_plays(recent_plays):
    return [{"name": s["track"]["name"], "id":s["track"]["id"], "played_at":s["played_at"]}
            for s in recent_plays["items"]]


def get_spotify(username: str, cache_path: str) -> spotipy.Spotify:
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        username=username,
                        cache_path=cache_path,
                        redirect_uri="http://localhost:8888/callback")

    return spotipy.Spotify(auth_manager=auth)

def first_fetch(user):
    history = {}
    user_db_path = f"./db/{user['id']}-history.json"

    sp = get_spotify(username=user["name"], cache_path=f"db/{user['id']}.token")
    recent_plays = sp.current_user_recently_played()

    recent_songs = parse_recent_plays(recent_plays)
    print(f"Found {len(recent_songs)} new songs")

    # get new latest song to update db
    latest = utils.to_utc_m(recent_songs[0]["played_at"])

    # update last fetch
    history["last_fetch"] = latest

    # update with new songs
    history["songs"] = recent_songs

    # save
    utils.save_json(history, user_db_path)

    return recent_songs[-1]


def update_with_latest(user: dict):

    user_db_path = f"./db/{user['id']}-history.json"

    # load user history
    history = utils.load_json(user_db_path)

    # get users latest song
    latest = history.get("last_fetch") # most recent song played at time

    print(f"getting tracks since latest {latest}")

    # set up spotify client for user
    sp = get_spotify(username=user["name"], cache_path=f"db/{user['id']}.token")

    # Get and parse recent plays
    recent_plays = sp.current_user_recently_played(after=latest)

    if len(recent_plays["items"]) > 0:

        recent_songs = parse_recent_plays(recent_plays)
        print(f"Found {len(recent_songs)} new songs")

        # get new latest song to update db
        latest = utils.to_utc_m(recent_songs[0]["played_at"])

        # update last fetch
        history["last_fetch"] = latest

        # update with new songs
        current_songs = history["songs"] # NOTE: can probably get rid of this
        history["songs"] = recent_songs + current_songs

        # save
        utils.save_json(history, user_db_path)



def sync_data():
    # get users
    users = utils.load_json("./db/users.json")

    for user in users["users"]:
        try:
            print(f"Fetching songs for {user['name']}")
            update_with_latest(user)
        except Exception as e:
            print(f"Failed getting latest songs for user['name']")
            print(e)





#NOTE: sceduling
# https://stackoverflow.com/questions/21214270/how-to-schedule-a-function-to-run-every-hour-on-flask
