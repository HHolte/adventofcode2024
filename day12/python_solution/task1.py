from numpy import array


def is_out_of_bounds(pos, puzzle):
    return not 0 <= pos[0] < puzzle.shape[0] or not 0 <= pos[1] < puzzle.shape[1]


def get_plots_in_same_region(pos, puzzle, plots_in_region: list[str], perimeter: int):
    plots_in_region.append(pos)
    adjacent_positions = [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]
    for adj_pos in adjacent_positions:
        if adj_pos in plots_in_region:
            continue
        if is_out_of_bounds(adj_pos, puzzle) or puzzle[adj_pos] != puzzle[pos]:
            perimeter += 1
            continue
        else:
            plots_in_region, perimeter = get_plots_in_same_region(adj_pos, puzzle, plots_in_region, perimeter)
    return plots_in_region, perimeter


def solve_first_task(file):
    total_price = 0
    puzzle = array([array([el for el in line.strip()]) for line in file])
    plots_used_in_region = []
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            if (i, j) in plots_used_in_region:
                continue
            plots_in_same_region, perimeter = get_plots_in_same_region((i, j), puzzle, [], 0)
            plots_used_in_region += plots_in_same_region
            total_price += len(plots_in_same_region) * perimeter
    return total_price


def main():
    data = open("day12/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
