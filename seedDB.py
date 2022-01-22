# --- 100 characters ------------------------------------------------------------------------------
# Created by: Shaun 2019/01/01

from utils import load_json
import boto3

def main():
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8888")

    #Add user
    print("adding User")
    userTable = dynamodb.Table('Users')

    new_user = {
        "id": "1231014939",
        "name": "Shaun Spinelli"
    }
    userTable.put_item(Item=new_user)

    # add songs
    print("Adding songs")
    songTable = dynamodb.Table('Songs')
    songs = load_json('db/songs.json')

    for song in songs:
        print(song)
        songTable.put_item(
            Item=song
        )


if __name__ == "__main__":
    main()
