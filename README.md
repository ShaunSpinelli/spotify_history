# Spotify history tracking app

live on [heroku](https://spotify-hist.herokuapp.com/)


## Release with heroku

1 - Build and push

```
heroku container:push web -a spotify-hist

```

2 - Deploy

```
heroku container:release web -a spotify-hist
```

3 - Get logs

```
heroku logs -t -a spotify-hist
```


4 - ssh into box on heroku

```
heroku run bash -a spotify-hist
```


## Lambda stuff

```
pip3 install --target ./package

zip -r ../my-deployment-package.zip .

```

## Development

Setting up dev environment with [moto](https://github.com/spulec/moto)

start dynamodb server

```
moto_server dynamodb2
```

create tables run

```
python3 db/moto_db.py
```
