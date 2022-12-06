def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def find_first_unique_sequence(lst, n=4):
    for i in range(0, len(lst) - n):
        window = lst[i:i+n]
        print(f"{i}: {window}")
        if len(set(window)) == n:
            return i+n


if __name__ == "__main__":
    data = input_data("data/input.txt")
    print(data)

    # part 1
    print(find_first_unique_sequence(data[0], 4))

    # part 2
    print(find_first_unique_sequence(data[0], 14))
