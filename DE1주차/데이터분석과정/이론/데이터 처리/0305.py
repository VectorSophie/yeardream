import pandas as pd
import numpy as np

def get_mean(df: pd.DataFrame) -> float:
    
    score_mean = df.score.mean()
    return score_mean

def get_median(df: pd.DataFrame) -> float:
    
    score_median = df.score.median()
    return score_median

def get_std(df: pd.DataFrame) -> float:

    score_std = df.score.std()
    return score_std

def main():
    DATA_PATH = "test.csv"

    df = pd.read_csv(DATA_PATH)

    mean = get_mean(df)
    print("평균:", mean)

    median = get_median(df)
    print("중앙값:", median)

    std = get_std(df)
    print("표준편차:", std)

if __name__ == "__main__":
    main()
