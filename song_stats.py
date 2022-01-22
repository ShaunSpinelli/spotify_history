import pandas as pd


def get_song_stats(songs):
    df = pd.DataFrame.from_dict(songs)
    df.columns = ['id', 'name', 'song', 'time', 'user']
    df['time'] = pd.to_datetime(df['time'])
    df['weekday'] = df['time'].dt.dayofweek
    df.set_index('time', inplace=True)
    df["artist"] = [s.split("-")[-1].strip() for s in df.name]

    results = {}

    results["artists_count"] = df['artist'].value_counts().to_dict()
    results["songs_count"] = df['name'].value_counts().to_dict()
    results["week_songs"] = df.last('3D').weekday.value_counts().to_dict()
    results["month_songs"] = df.last('1M').weekday.value_counts().to_dict()

    return results
