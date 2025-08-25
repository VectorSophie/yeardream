import pandas as pd

DATA_PATH = "train.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    df.info()

    print(df.head())

    print(df.describe())

    print(df["Survived"].value_counts())

if __name__ == "__main__":
    main()
