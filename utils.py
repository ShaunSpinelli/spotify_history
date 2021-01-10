import json
import uuid
from dateutil.parser import parse


import typing as t

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


def setup_new_user(user):
    id = str(uuid.uuid4())
    return {"id": id, "name": user["display_name"] }

