import pandas as pd
import numpy as np

def slicing(data: pd.Series):

    data = data[1:4]
    return data

def main():

    data = pd.Series(range(5), index=["A", "B", "C", "D", "E"])

    data = slicing(data)

    print(data)

    return 0

if __name__ == "__main__":
    main()
