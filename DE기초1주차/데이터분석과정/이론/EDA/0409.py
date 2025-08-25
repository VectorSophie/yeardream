import numpy as np
import pandas as pd

DATA_PATH = "train.csv"

def drop_nan(df: pd.DataFrame) -> pd.DataFrame:

    df = df.dropna()
    return df

def interpolate_data(df: pd.DataFrame):

    df["Age"] = df["Age"].interpolate()
    return df

def get_data() -> pd.DataFrame:

    df = pd.read_csv(DATA_PATH)
    return df

def main():

    df = get_data()
    print("전처리 전 데이터 수:", len(df))

    df_drop = drop_nan(df.copy())
    print("결측치 제거 후 데이터 수:", len(df_drop))

    df_itp = interpolate_data(df.copy())
    print("결측치 보간 후 데이터 수:", len(df_itp))

if __name__ == "__main__":
    main()
