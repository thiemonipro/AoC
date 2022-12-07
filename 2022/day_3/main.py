import string

letters_value = {letter: index+1 for index, letter in enumerate(string.ascii_letters)}


def split_in_half(lst):
    amount_elements = len(lst)
    half = int(amount_elements/2)
    return lst[:half], lst[amount_elements-half:]

def batch(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def determine_value(lhs, rhs):
    lhs = set(lhs)
    rhs = set(rhs)
    print(f"{lhs=}")
    print(f"{rhs=}")
    intersection = lhs.intersection(rhs)
    print(f"{intersection=}")
    return sum(letters_value[letter] for letter in intersection)

def determine_value_2(e1, e2, e3):
    e1 = set(e1)
    e2 = set(e2)
    e3 = set(e3)
    intersection = e1.intersection(e2)
    intersection = intersection.intersection(e3)
    return sum(letters_value[letter] for letter in intersection)


def process_data(data):
    value = 0
    for rugsack in data:
        compartiment_1, compartiment_2 = split_in_half(rugsack)
        value += determine_value(compartiment_1, compartiment_2)
    return value


def process_data_2(data):
    value = 0
    groups = batch(data, 3)
    for group in groups:
        elve1 , elve2, elve3 = group
        value += determine_value_2(elve1, elve2, elve3)
    return value


if __name__ == "__main__":
    data = input_data("data/input.txt")

    # day 1
    print(process_data(data))

    # day 2
    print(process_data_2(data))