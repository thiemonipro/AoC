from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


@dataclass
class Directory:
    name: str
    parent: str
    subdirectories: list
    files: list

    def get_size(self):
        file_size = sum(file.size for file in self.files)
        directories_size = sum(directory.get_size() for directory in self.subdirectories)
        return file_size+directories_size

    def pretty_print(self):
        print(f"HEAD: {self.name}: {self.get_size()}")
        for directory in self.subdirectories:
            print(f"dir: {directory.name}: {directory.get_size()}")

        for file in self.files:
            print(f"file: {file.name} : {file.size}")


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def process_data(lines):
    root_dir = Directory("/", 0, [], [])
    directories = [root_dir]
    current_dir = root_dir

    for line in lines:
        if line.startswith("dir"): continue

        elif line.startswith("$ cd"):
            print(f"changing current directory")
            dir_name = line.split("cd ")[1]
            if dir_name == "..":
                current_dir = current_dir.parent
            elif dir_name == "/": continue
            else:
                new_dir = Directory(dir_name, current_dir, [], [])
                current_dir.subdirectories.append(new_dir)
                current_dir = new_dir
                directories.append(current_dir)

        elif line.split(" ")[0].isdigit():
            size, name = line.split(" ")
            current_dir.files.append(File(name, size))

    return directories


if __name__ == "__main__":
    data = input_data("data/input.txt")
    directories = process_data(data)

    # part 1
    print(f"part 1: {sum([directory.get_size() for directory in directories if directory.get_size() <= 100000])}")

    # part 2
    total_space = 70000000
    needed_space = 30000000
    current_free_space = total_space-directories[0].get_size()

    space_to_clear = needed_space - current_free_space

    print(f"need to clear: {space_to_clear} bytes")

    possible_directories = [directory for directory in directories if directory.get_size() >= space_to_clear]
    smallest_directory = sorted(possible_directories, key=lambda x: x.get_size())[0]
    smallest_directory.pretty_print()