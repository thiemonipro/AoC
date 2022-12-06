def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def process_data(data: list):
    elve_calories = []
    counter = 0
    for value in data:
        if value != "":
            counter += int(value)
        else:
            elve_calories.append(counter)
            counter = 0

    elve_calories.sort(reverse=True)
    return elve_calories


if __name__ == "__main__":
    data = input_data("data/input.txt")
    elve_calories = process_data(data)

    print(elve_calories[0])
    print(sum(elve_calories[:3]))