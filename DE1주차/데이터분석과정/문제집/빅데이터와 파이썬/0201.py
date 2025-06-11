import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    
    df = pd.read_csv(path)
    return df

def concat_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.concat([df1,df2])
    df = df.reset_index(drop=True)
    return df

def add_rank(df: pd.DataFrame) -> pd.DataFrame:

    df["rank"] = df.score.rank(ascending=False)
    df = df.sort_values(by="rank")
    df = df.reset_index(drop=True)
    return df

def get_new_class(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:

    df_high = df[df["rank"]<=30]
    df_low = df[df["rank"]>30]

    return df_high, df_low

def main():
    CLASS1 = "class1.csv"
    CLASS2 = "class2.csv"

    df1 = load_data(CLASS1)
    df2 = load_data(CLASS2)

    df = concat_data(df1, df2)

    df = add_rank(df)

    df_high, df_low = get_new_class(df)
    print("심화반" + "=" * 20)
    print(df_high)

    print("기초반" + "=" * 20)
    print(df_low)

if __name__ == "__main__":
    main()
