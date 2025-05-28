import pandas as pd
import numpy as np

KOR_COL_NAME = {"name": "이름", "age": "나이", "adult": "성인여부"}

def add_adult(df: pd.DataFrame) -> pd.DataFrame:
 
    df["adult"] = df["age"]>=18
    return df

def rename_kor(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.rename(columns=KOR_COL_NAME)
    return df

def main():
    data = pd.DataFrame()
    data["name"] = ["James", "John", "Sarah", "Michael"]
    data["age"] = [19, 20, 18, 31]

    df = add_adult(data)
    print(df)

    df = rename_kor(df)
    print(df)

if __name__ == "__main__":
    main()