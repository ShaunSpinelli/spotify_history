# --- 100 characters ------------------------------------------------------------------------------
# Created by: Shaun 2019/01/01

"""Stats Middleware Stuff"""

import pandas as pd


def preprocess_songs(songs, UTC_offset=10):
    # Create df
    df = pd.DataFrame.from_dict(songs)

    # Add time information
    df['time'] = pd.to_datetime(df['unix_time'], unit="s") + pd.DateOffset(hours=UTC_offset)
    df['month'] = df['time'].dt.month
    df['weekday'] = df['time'].dt.dayofweek
    df['day_of_year'] = df['time'].dt.dayofyear
    df.set_index('time', inplace=True)
    df['hour_of_day'] = df.index.hour

    df["artist"] = [s.split("-")[-1].strip() for s in df.name]
    # need to sort so pandas doesnt break
    df.sort_values(by="time", ascending=True, inplace=True)

    return df


def artist_listen_count_over_time(df, time, count):
    return df.last(time).artist.value_counts().head(n=count).to_dict()


