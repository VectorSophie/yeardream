import numpy as np

def make_array() -> np.ndarray:
    array = np.arange(1,201)
    return array


def reshape_array(ar: np.ndarray) -> np.ndarray:
    array = ar.reshape(25,8)
    return array


def main():
    ar = make_array()
    print(ar.shape)

    ar = reshape_array(ar)
    print(ar.shape)


if __name__ == "__main__":
    main()