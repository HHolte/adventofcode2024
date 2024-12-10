from typing import Callable
from numpy import array


def get_antenna_positions(puzzle):
    antennas = {}
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            symbol = puzzle[i, j]
            if symbol == ".":
                continue
            if symbol not in antennas:
                antennas[symbol] = [(i, j)]
            else:
                antennas[symbol].append((i, j))
    return antennas


def antinode_is_within_bounds(antinode, puzzle):
    return 0 <= antinode[0] < puzzle.shape[0] and 0 <= antinode[1] < puzzle.shape[1]


def calculate_antinodes_task1(a: tuple[int, int], b: tuple[int, int], puzzle):
    distance = (a[0] - b[0], a[1] - b[1])
    first_antinode = (a[0] + distance[0], a[1] + distance[1])
    second_antinode = (b[0] - distance[0], b[1] - distance[1])
    return [antinode for antinode in [first_antinode, second_antinode] if antinode_is_within_bounds(antinode, puzzle)]


def solve_first_task(file, calculate_antinodes: Callable):
    puzzle = array([array(list(line.strip())) for line in file])
    antennas = get_antenna_positions(puzzle)
    antinode_locations = []
    for antennas in antennas.values():
        antenna = antennas.pop(0)
        while antennas:
            for other_antenna in antennas:
                antinode_locations += calculate_antinodes(antenna, other_antenna, puzzle)
            antenna = antennas.pop(0)
    return len(set(antinode_locations))


def main():
    data = open("day8/test_data.txt", "r")

    solution = solve_first_task(data, calculate_antinodes_task1)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
