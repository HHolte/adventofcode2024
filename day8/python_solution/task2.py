from math import floor
from numpy import array, any as npany
from task1 import antinode_is_within_bounds, solve_first_task


def get_antinodes(root_node, distance, puzzle):
    antinodes = [root_node]
    next_antinode = (root_node[0] + distance[0], root_node[1] + distance[1])
    while antinode_is_within_bounds(next_antinode, puzzle):
        antinodes.append(next_antinode)
        next_antinode = (next_antinode[0] + distance[0], next_antinode[1] + distance[1])
    return antinodes


def calculate_antinodes_task2(a: tuple[int, int], b: tuple[int, int], puzzle):
    antinodes = []
    distance = array([a[0] - b[0], a[1] - b[1]])
    rate = max(distance) / min(distance) if 1 not in distance and -1 not in distance else 1
    unit_distance = distance / rate if rate / floor(rate) == 1 else distance
    antinodes += get_antinodes(a, unit_distance, puzzle)
    antinodes += get_antinodes(b, -unit_distance, puzzle)
    if npany(unit_distance != distance):
        node_between = (a[0] - unit_distance[0], a[1] - unit_distance[1])
        while node_between != b:
            antinodes.append(node_between)
            node_between = (node_between[0] - unit_distance[0], node_between[1] - unit_distance[1])
    return antinodes


def solve_second_task(file):
    return solve_first_task(file, calculate_antinodes_task2)


def main():
    data = open("day8/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
