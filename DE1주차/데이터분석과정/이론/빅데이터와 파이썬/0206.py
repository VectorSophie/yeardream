import pandas as pd

def get_oldest(df: pd.DataFrame) -> str:
    
    index = df.age.argmax()
    name = df.loc[index,"name"]
    return name

def get_youngest(df: pd.DataFrame) -> str:
    
    index = df.age.argmin()
    name = df.loc[index,"name"]
    return name

def main():
    
    data = pd.DataFrame(columns=["name", "age"])
    data["name"] = ["Ani", "James", "Kane", "Kim", "Teddy"]
    data["age"] = [15, 19, 26, 52, 30]

    oldest = get_oldest(data)
    print(oldest)

    youngest = get_youngest(data)
    print(youngest)

if __name__ == "__main__":
    main()
