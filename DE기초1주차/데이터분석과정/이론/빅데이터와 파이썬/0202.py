import pandas as pd
import numpy as np

def indexing(data: pd.Series):
    
    data = data['C']
    return data


def main():

    data = pd.Series(range(5), index=["A", "B", "C", "D", "E"])

    data = indexing(data)

    print(data)

    return 0

if __name__ == "__main__":
    main()
