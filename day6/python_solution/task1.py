from numpy import array, where


def get_guard_and_obstacle_positions(puzzle):
    guard = where(puzzle == "^")
    obstacles = where(puzzle == "#")
    guard_position = (guard[0][0], guard[1][0])
    obstacles_positions = [(obstacles[0][i], obstacles[1][i]) for i in range(len(obstacles[0]))]
    return guard_position, obstacles_positions


guard_rotations = {
    "U": "R",
    "R": "D",
    "D": "L",
    "L": "U"
}


def position_is_outside_map(position, puzzle):
    return not -1 < position[0] < puzzle.shape[0] or not -1 < position[1] < puzzle.shape[1]


def update_guard_position(current_position, direction):
    match direction:
        case "U":
            return (current_position[0] - 1, current_position[1])
        case "D":
            return (current_position[0] + 1, current_position[1])
        case "L":
            return (current_position[0], current_position[1] - 1)
        case "R":
            return (current_position[0], current_position[1] + 1)


def solve_first_task(puzzle):
    guard_position, obstacle_positions = get_guard_and_obstacle_positions(puzzle)
    puzzle[guard_position] = "X"
    direction = "U"
    while True:
        new_guard_position = update_guard_position(guard_position, direction)
        if new_guard_position in obstacle_positions:
            direction = guard_rotations[direction]
            continue
        elif position_is_outside_map(new_guard_position, puzzle):
            break
        guard_position = new_guard_position
        puzzle[guard_position] = "X"
    return where(puzzle == "X")


def main():
    data = open("day6/test_data.txt", "r")

    puzzle = array([array(list(line.strip())) for line in data])
    positions_visited = solve_first_task(puzzle)
    solution = len(positions_visited[0])
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
