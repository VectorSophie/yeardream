import pandas as pd
import numpy as np

def print_info(df: pd.DataFrame) -> None:

    print("결측치:", df.score.isna().sum())
    print("이상치:", len(df[df["spent_time"] > 3600]))


def replace_spent_time(df: pd.DataFrame) -> pd.DataFrame:

    df[df["spent_time"]>3600] = 3600
    return df


def fill_score(df: pd.DataFrame) -> pd.DataFrame:
    
    df["score"] = df["score"].fillna(0)
    return df

def main():
    DATA_PATH = "test_log.csv"

    df_log = pd.read_csv(DATA_PATH)
    print("==수정전==")
    print_info(df_log)

    df_log = replace_spent_time(df_log)

    df_log = fill_score(df_log)

    print("==수정후==")
    print_info(df_log)

if __name__ == "__main__":
    main()
