import pandas as pd

WEEK_KOR = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

def load_csv(path: str) -> pd.DataFrame:
    
    df = pd.read_csv(path)
    return df

def cvt_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    return df

def add_dayofweek(df: pd.DataFrame) -> pd.DataFrame:
    
    df["요일"] = df["DateTime"].dt.dayofweek
    df["요일"] = df["요일"].map(WEEK_KOR)
    return df

def get_mean_consumption(df: pd.DataFrame) -> pd.Series:
   
    series_mean = df.groupby("요일")["Consumption"].mean()
    return series_mean

def main():

    data_path = "data/electronic.csv"

    df = load_csv(data_path)

    df = cvt_to_datetime(df)
    print(df)

    df = add_dayofweek(df)
    print(df)

    s_mean = get_mean_consumption(df)
    print(s_mean)

if __name__ == "__main__":
    main()
