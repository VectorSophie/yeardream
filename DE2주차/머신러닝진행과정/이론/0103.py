import pandas as pd
import numpy as np

DATA_PATH = 'data/taxi_fare_data.csv'

def load_csv(path):
    data_frame = pd.read_csv(path)
    return data_frame

df = load_csv(DATA_PATH)

print("누락된 데이터(Missing Data)를 제거하기 전의 데이터 정보")
df.info()

del_un_df = df.drop(["Unnamed: 0"],axis=1)

del_un_id_df = del_un_df.drop(["id"],axis=1)

removed_df = del_un_id_df.dropna()
print("\n결측치(Missing Data)를 제거한 후의 데이터 정보")
removed_df.info()