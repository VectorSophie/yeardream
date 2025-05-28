import pandas as pd

def concat_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    df_new = pd.concat([df1,df2])
    df_new = df_new.reset_index(drop=True)
    return df_new


def merge_data(df_log: pd.DataFrame, df_name: pd.DataFrame) -> pd.DataFrame:

    df_new = pd.merge(df_log,df_name, on="student_id")
    return df_new

def main():
    CLASS1_PATH = "class1.csv"
    CLASS2_PATH = "class2.csv"
    NAME_PATH = "name.csv"

    df_class1 = pd.read_csv(CLASS1_PATH)
    df_class2 = pd.read_csv(CLASS2_PATH)
    df_name = pd.read_csv(NAME_PATH)

    df_all = concat_data(df_class1, df_class2)
    print(df_all)

    df_merged = merge_data(df_all, df_name)
    print(df_merged)

if __name__ == "__main__":
    main()