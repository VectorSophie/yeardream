import pandas as pd
import numpy as np

def extracting(data: pd.Series) -> pd.Series:

    data = data[data%2==0]
    return data

def main():

    data = pd.Series(range(5), index=["A", "B", "C", "D", "E"])

    data = extracting(data)

    print(data)

    return 0

if __name__ == "__main__":
    main()
