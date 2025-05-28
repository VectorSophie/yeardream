import pandas as pd
import numpy as np

def get_corr(df: pd.DataFrame) -> float:

    corr = np.corrcoef(df["키"],df["몸무게"])[0][1]
    return float(corr)

def main():

    df = pd.DataFrame(
        {"키": [158, 163, 170, 172, 180, 163], "몸무게": [49, 52, 60, 80, 83, 55]}
    )

    corr = get_corr(df)
    print("키와 몸무게의 상관계수:", corr)

if __name__ == "__main__":
    main()
