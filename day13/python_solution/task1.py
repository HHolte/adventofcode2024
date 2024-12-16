from itertools import islice


class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]

    def __init__(self, lines):
        self.button_a = self.get_button(lines[0])
        self.button_b = self.get_button(lines[1])
        self.prize = self.get_prize(lines[2])

    def get_button(self, line):
        x, y = line.strip().split(":")[1].split(",")
        return (int(x.split("+")[1]), int(y.split("+")[1]))

    def get_prize(self, line):
        x, y = line.strip().split(":")[1].split(",")
        return (int(x.split("=")[1]), int(y.split("=")[1]))


# Implementation assumes there is a unique solution for each machine, which is equivalent to assuming
# that the system of equations used to describe each machine is linearly independent
def calculate_token_sum(machine: Machine, offset_prize: int = 0):
    a_x, a_y = machine.button_a
    b_x, b_y = machine.button_b
    p_x, p_y = machine.prize
    p_x += offset_prize
    p_y += offset_prize

    t = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)
    if t != int(t):
        return 0

    s = (p_x - t * b_x) / a_x
    if s != int(s):
        return 0

    return int(3 * s + t)


def solve_first_task(file):
    token_sum = 0
    while True:
        next_four_lines = list(islice(file, 4))
        if not next_four_lines:
            break
        machine = Machine(next_four_lines[:3])
        token_sum += calculate_token_sum(machine)
    return token_sum


def main():
    data = open("day13/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
