# Spotify history tracking app


## Release with heroku

1 - Build and push

```
heroku container:push web -a spotify-hist

```

2 - Release

```
heroku container:release web -a spotify-hist
```

3 - Get logs

```
heroku logs -t -a spotify-hist
```


4 - ssh into box

```
heroku run bash -a spotify-hist
```
