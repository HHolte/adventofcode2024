from task1 import find_next_positions
from numpy import array, where


def find_trails(position, trail_map):
    if trail_map[position[0], position[1]] == 9:
        return 1
    next_trail_positions = find_next_positions(position, trail_map)
    n_trails = 0
    for next_position in next_trail_positions:
        n_trails += find_trails(next_position, trail_map)
    return n_trails


def solve_second_task(file):
    summ = 0
    puzzle = array([array([int(el) for el in line.strip()]) for line in file])
    zeros = where(puzzle == 0)
    zero_positions = [array([zeros[0][i], zeros[1][i]]) for i in range(len(zeros[0]))]
    for zero in zero_positions:
        summ += find_trails(zero, puzzle)
    return summ


def main():
    data = open("day10/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
