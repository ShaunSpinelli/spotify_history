# --- 100 characters ------------------------------------------------------------------------------
# Created by: Shaun 2019/01/01

"""Stats Middleware Stuff"""

import pandas as pd
import numpy as np

def normalise(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


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


def hour_of_day_listen_times_array(df, key):
    daily_list_times = df.groupby([key])["hour_of_day"].value_counts().to_dict()

    listen_x = max(df[key]) + 1

    day_time_tuples = [ele for key in daily_list_times for ele in key]

    year_listening_times = np.zeros((24, listen_x))

    for idx in range(0, len(day_time_tuples), 2):
        day, hour = day_time_tuples[idx: idx + 2]
        v = daily_list_times[(day, hour)]
        year_listening_times[hour][day] = v

    normed = normalise(year_listening_times).tolist()
    shape = year_listening_times.shape
    return {"shape": shape, "data": normed}
