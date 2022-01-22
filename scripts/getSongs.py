# --- 100 characters ------------------------------------------------------------------------------
# Created by: Shaun 2019/01/01

import boto3
import json
from dateutil.parser import parse
from boto3.dynamodb.conditions import Key
import dateutil

DYNAMODB_ENDPOINT = 'https://dynamodb.us-west-2.amazonaws.com'
ACCESS_KEY =''
SECRET_KEY =''

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)



def load_json(path:str) -> dict:
    with open(path) as f:
        data = json.load(f)
    return data



def save_json(data: dict, path:str) -> None:
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def to_utc_m(timestamp: str) -> int:
    """Converts to  ISO 8601  time stamp unix timestamp in milliseconds."""
    dt = parse (timestamp)
    utc_m = dt.timestamp() * 1000
    return int(utc_m)


def get_users_songs(user_id):
    # dynamodb = client.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)

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

    save_json(history,"shaun-songs.json")


def main():
    get_users_songs('1231014939')

if __name__ == '__main__':
    main()
