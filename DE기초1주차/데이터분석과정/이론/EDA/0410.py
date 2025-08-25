import numpy as np
import pandas as pd

DATA_PATH = "data.csv"

def get_data() -> pd.DataFrame:

    df = pd.read_csv(DATA_PATH)
    return df

def add_type(df: pd.DataFrame) -> pd.DataFrame:

    df["Type"]=np.where(df["Age"]>=19,"adult","kid")
    df.loc[(df["Age"]<19)&(df["Sex"]=="female"), "Type"] = "girl"
    df.loc[(df["Age"]<19)&(df["Sex"]=="male"), "Type"] = "boy"
    return df

def main():

    df = get_data()
    print("추가 전\n", df.head())

    df_new = add_type(df.copy())
    print("추가 후\n", df_new.head())

if __name__ == "__main__":
    main()
