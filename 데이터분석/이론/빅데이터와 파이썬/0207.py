import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)
    return df


def get_ranking(df: pd.DataFrame) -> pd.DataFrame:
    
    df["rank"] = df.score.rank(ascending=False)
    return df

def main():
    DATA_PATH = "score.csv"

    df = load_data(DATA_PATH)

    df_rank = get_ranking(df)
    print(df_rank)

if __name__ == "__main__":
    main()