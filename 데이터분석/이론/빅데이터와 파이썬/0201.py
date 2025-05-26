import numpy as np

def transforms(data: np.ndarray) -> np.ndarray:
    data = np.where(data>19, "adult","kid")
    return data

def main():

    data = np.array([40, 12, 54, 64, 13, 76, 9, 23, 18, 19, 67, 85, 51])

    data = transforms(data)

    print(data)

    return 0

if __name__ == "__main__":
    main()
