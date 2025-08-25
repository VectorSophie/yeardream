def plus_one(value):
    value = int(value)

    value += 1
    return value


def main():
    value = input()

    result = plus_one(value)

    print(result)


if __name__ == "__main__":
    main()