# def first_fetch(user):
#     history = {}
#     user_db_path = f"./db/{user['id']}-history.json"
#
#     sp = get_spotify(username=user["name"], cache_path=f"db/{user['id']}.token")
#     recent_plays = sp.current_user_recently_played()
#
#     recent_songs = parse_recent_plays(recent_plays)
#     print(f"Found {len(recent_songs)} new songs")
#
#     # get new latest song to update db
#     latest = to_utc_m(recent_songs[0]["played_at"])
#
#     # update last fetch
#     history["last_fetch"] = latest
#
#     # update with new songs
#     history["songs"] = recent_songs
#
#     # save
#     utils.save_json(history, user_db_path)
#
#     return recent_songs[-1]




import os
import time
import json
import boto3
import spotipy
from dateutil.parser import parse
from spotipy.oauth2 import SpotifyOAuth


# Spotify Related Config
APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SCOPE = "user-read-recently-played"


dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:5000")

def save_json(data: dict, path:str) -> None:
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def to_utc_m(timestamp: str) -> int:
    """Converts to  ISO 8601  time stamp unix timestamp in milliseconds."""
    dt = parse (timestamp)
    utc_m = dt.timestamp() * 1000
    return int(utc_m)


def get_users():
    """Returns all users"""
    table = dynamodb.Table('Users')
    response = table.scan()

    return response["Items"]

def parse_recent_plays(recent_plays, user_id):
    return [{"name": s["track"]["name"], "id":s["track"]["id"], "played_at":s["played_at"], "user": user_id}
            for s in recent_plays["items"]]


def get_spotify(username: str, cache_path: str) -> spotipy.Spotify:
    auth = SpotifyOAuth(client_id=APP_CLIENT_ID,
                        client_secret=APP_CLIENT_SECRET,
                        scope=SCOPE,
                        username=username,
                        cache_path=cache_path,
                        redirect_uri="http://localhost:8888/callback")

    return spotipy.Spotify(auth_manager=auth)


def add_songs(songs):

    table = dynamodb.Table('Songs')

    for song in songs:
        response = table.put_item(
            Item=song
        )


def update_user_latest(latest, user):

    table = dynamodb.Table('Users')
    print("updating")
    response = table.update_item(
        Key={
            'id': user["id"],
            "user": user["name"]
        },
        UpdateExpression="set last_fetch = :r",
        ExpressionAttributeValues={
            ':r': latest,
        },
        ReturnValues="UPDATED_NEW"
    )

    return response


def update_with_latest(user: dict):


    # get users latest song
    latest = user.get("last_fetch", None) # most recent song played at time

    print(f"getting tracks since latest {latest}")

    # set up spotify client for user

    token_path = "./token.tok"

    user["token"]["expires_in"] = int(user["token"]["expires_in"])
    user["token"]["expires_at"] = int(user["token"]["expires_at"])

    save_json(user["token"], token_path)

    sp = get_spotify(username=user["name"], cache_path=token_path)

    # Get and parse recent plays
    recent_plays = sp.current_user_recently_played(after=latest)

    if len(recent_plays["items"]) > 0:

        recent_songs = parse_recent_plays(recent_plays, user["id"])
        print(f"Found {len(recent_songs)} new songs")

        # get new latest song to update db
        latest = to_utc_m(recent_songs[0]["played_at"])

        # update last fetch
        u = update_user_latest(latest, user)

        # update with new songs
        add_songs(recent_songs)





def sync_data():
    # get users
    users = get_users()

    for user in users:
        try:
            print(f"Fetching songs for {user['name']}")
            update_with_latest(user)
        except Exception as e:
            print(f"Failed getting latest songs for {user['name']}")
            print(e)



if __name__ == '__main__':
    sync_data()
    # print(get_users())
