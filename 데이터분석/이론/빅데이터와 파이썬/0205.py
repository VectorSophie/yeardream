import pandas as pd

def get_adults(df: pd.DataFrame) -> pd.DataFrame:

    df_adults = df[df.Age>=20]
    return df_adults

def main():

    data = pd.DataFrame(columns=["Email", "Name", "Age"])
    data["Name"] = ["doori", "minsu", "james"]
    data["Email"] = ["doori@gmail.com", "minsu@gmail.com", "james@gmail.com"]
    data["Age"] = [16, 20, 25]

    df_adults = get_adults(data)
    print(df_adults)

if __name__ == "__main__":
    main()
