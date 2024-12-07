from task1 import get_guard_and_obstacle_positions, position_is_outside_map, solve_first_task, update_guard_position
from numpy import array


guard_rotations = {
    "U": "R",
    "R": "D",
    "D": "L",
    "L": "U"
}


def guard_is_in_loop(puzzle, guard_position, obstacle_positions):
    guard_is_looping = False
    direction = "U"
    obstacles_encountered = []
    while not guard_is_looping:
        new_guard_position = update_guard_position(guard_position, direction)
        if new_guard_position in obstacle_positions:
            if (new_guard_position, direction) in obstacles_encountered:
                guard_is_looping = True
            obstacles_encountered.append((new_guard_position, direction))
            direction = guard_rotations[direction]
            continue
        elif position_is_outside_map(new_guard_position, puzzle):
            break
        guard_position = new_guard_position
    return guard_is_looping


def solve_second_task(file):
    number_of_loops = 0
    puzzle = array([array(list(line.strip())) for line in file])
    guard_position, obstacle_positions = get_guard_and_obstacle_positions(puzzle)
    positions_visited = solve_first_task(puzzle)
    possible_obstacle_positions = [(i, j) for i, j in zip(positions_visited[0], positions_visited[1])]
    possible_obstacle_positions.remove(guard_position)
    print("Positions to check: ", len(possible_obstacle_positions))
    for position in possible_obstacle_positions:
        print("Checking position: ", position)
        obstacle_positions.append(position)
        number_of_loops += guard_is_in_loop(puzzle, guard_position, obstacle_positions)
        obstacle_positions.pop(-1)
    return number_of_loops


def main():
    data = open("day6/ex_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
