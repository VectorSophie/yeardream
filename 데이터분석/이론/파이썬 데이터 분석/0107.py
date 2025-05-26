import numpy as np

def filter_3(array: np.ndarray) -> np.ndarray:
    ar = array[array%3==0]
    return ar


def get_stat(array: np.ndarray):
    mean = array.mean()
    var = array.var()

    return mean, var


def main():
    ar = np.arange(1, 67)

    ar = filter_3(ar)
    print(ar)

    mean, var = get_stat(ar)
    print(mean, var)

if __name__ == "__main__":
    main()