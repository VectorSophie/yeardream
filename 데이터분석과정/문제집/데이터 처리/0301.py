import pandas as pd
import numpy as np

def drop_nan(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.dropna()
    return df

def get_male_survived(df: pd.DataFrame) -> int:
 
    df_male_surv = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
    return len(df_male_surv)


def get_died_20(df: pd.DataFrame) -> int:

    died_20 = df[(df['Survived'] == 0) & (df['Age'] >= 20) & (df['Age'] < 30)]
    return len(died_20)

def pclass1_survived_rate(df: pd.DataFrame) -> float:

    pclass1 = df[df['Pclass'] == 1]
    survived = pclass1[pclass1['Survived'] == 1]
    rate = len(survived) / len(pclass1)
    return rate

def main():
    DATA_PATH = "train.csv"

    df_train = pd.read_csv(DATA_PATH)
    print("전처리 전 데이터 수:", len(df_train))

    df_train = drop_nan(df_train)
    print("전처리 후 데이터 수:", len(df_train))

    male_survived = get_male_survived(df_train)
    print("남성 생존자수:", male_survived)

    died_20 = get_died_20(df_train)
    print("20대 사망자수:", died_20)

    survived_rate = pclass1_survived_rate(df_train)
    print("pclass 1의 생존자 비율:", survived_rate)

if __name__ == "__main__":
    main()
