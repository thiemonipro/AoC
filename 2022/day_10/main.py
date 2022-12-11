from dataclasses import dataclass

@dataclass
class Cpu:
    register: int = 1
    cycle_count: int = 0
    signal_strengths = []

    def cycle(self):
        self.register_singal_strengt()
        self.cycle_count += 1
        self.draw()

    def register_singal_strengt(self):
        self.signal_strengths.append(self.register)

    def add(self, n):
        for i in range(2):
            self.cycle()
        self.register += n

    def noop(self):
        self.cycle()

    def command(self, command):
        if command.startswith("noop"):
            self.noop()
        else:
            amount = command.split(" ")[1]
            self.add(int(amount))

    def draw(self):
        # draw line
        if self.cycle_count and self.cycle_count % 40 == 0:
            row_strengths = self.signal_strengths[self.cycle_count-40:]
            pixels = []
            for index, strength in enumerate(row_strengths):
                if strength -1 <= index  <= strength + 1:
                    pixels.append("#")
                else:
                    pixels.append(".")
            print(pixels)



def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    data = input_data("data/input.txt")

    # part 1
    cpu = Cpu()

    for command in data:
        cpu.command(command)

    important_cycles = [20, 60, 100, 140, 180, 220]
    singal_strength = [i*cpu.signal_strengths[i-1] for i in important_cycles]
    print(f"sum: {sum(singal_strength)}")

    # part 2

