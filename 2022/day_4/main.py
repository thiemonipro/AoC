from dataclasses import dataclass

@dataclass
class ElveShift:
    start: int
    end: int

    def __init__(self, data):
        start, end = data.split("-")
        self.start = int(start)
        self.end = int(end)

    def fully_overlaps(self, other):
        return self.start <= other.start and self.end >= other.end or other.start <= self.start and other.end >= self.end

    def partially_overlaps(self, other):
        return self.start <= other.start <= self.end or other.start <= self.start <= other.end


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def process_data(data):
    overlaps = 0
    for line in data:
        shift_1 , shift_2 = line.split(",")
        shift_1 = ElveShift(shift_1)
        shift_2 = ElveShift(shift_2)
        if shift_1.fully_overlaps(shift_2):
            #print(f"{shift_1=}")
            #print(f"{shift_2=}")
            overlaps += 1
    return overlaps

def process_data_2(data):
    overlaps = 0
    for line in data:
        shift_1 , shift_2 = line.split(",")
        shift_1 = ElveShift(shift_1)
        shift_2 = ElveShift(shift_2)
        if shift_1.partially_overlaps(shift_2):
            print(f"{shift_1=}")
            print(f"{shift_2=}")
            overlaps += 1
    return overlaps


if __name__ == "__main__":
    data = input_data("data/input.txt")

    # day 1
    print(process_data(data))

    # day 2
    print(process_data_2(data))