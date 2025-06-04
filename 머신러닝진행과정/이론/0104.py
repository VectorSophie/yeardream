import pandas as pd
import numpy as np

DATA_PATH = "./data/taxi_fare_data.csv"

df = pd.read_csv(DATA_PATH, quoting=3)

def del_missing(df):
    del_un_df = df.drop(['Unnamed: 0'], axis='columns')
    del_un_id_df = del_un_df.drop(['id'], axis='columns')
    removed_df = del_un_id_df.dropna()
    return removed_df

def get_negative_index(list_data):
    neg_idx = []
    for i, value in enumerate(list_data):
        if value < 0:
            neg_idx.append(list_data.index[i])
    return neg_idx

def outlier_index():
    idx_fare_amount = get_negative_index(fare_amount)
    idx_passenger_count = get_negative_index(passenger_count)

    idx_zero_distance = []
    idx = [i for i in range(len(passenger_count))]
    zipped = zip(idx, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)

    for i, x, y, _x, _y in zipped:
        if (x == _x) and (y == _y):
            idx_zero_distance.append(passenger_count.index[i])

    total_index4remove = list(set(idx_fare_amount + idx_passenger_count + idx_zero_distance))
    return total_index4remove

def remove_outlier(dataframe, list_idx):
    return dataframe.drop(list_idx)

df = del_missing(df)

fare_amount = df['fare_amount']
passenger_count = df['passenger_count']
pickup_longitude = df['pickup_longitude']
pickup_latitude = df['pickup_latitude']
dropoff_longitude = df['dropoff_longitude']
dropoff_latitude = df['dropoff_latitude']

print('이상치를 제거하기 전의 데이터:')
df.info()

remove_index = outlier_index()
new = remove_outlier(df, remove_index)

print('\n이상치를 제거한 후의 데이터:')
new.info()
