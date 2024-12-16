from itertools import islice
from task1 import Machine, calculate_token_sum


def solve_second_task(file):
    offset = 10000000000000
    token_sum = 0
    while True:
        next_four_lines = list(islice(file, 4))
        if not next_four_lines:
            break
        machine = Machine(next_four_lines[:3])
        token_sum += calculate_token_sum(machine, offset)
    return token_sum


def main():
    data = open("day13/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
