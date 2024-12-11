from numpy import array, where, any as npany, all as npall


def position_is_valid(position, new_position, trail_map):
    if not 0 <= new_position[0] < trail_map.shape[0] or not 0 <= new_position[1] < trail_map.shape[1]:
        return False
    if trail_map[new_position[0], new_position[1]] - trail_map[position[0], position[1]] == 1:
        return True
    return False


def find_next_positions(position, trail_map):
    new_positions = [position + [0, 1], position + [1, 0], position - [0, 1], position - [1, 0]]
    relevant_positions = [pos for pos in new_positions if position_is_valid(position, pos, trail_map)]
    return relevant_positions


def find_trails(position, trail_map, nines_reached):
    if trail_map[position[0], position[1]] == 9:
        if len(nines_reached) == 0 or not npany([npall(ar) for ar in nines_reached == position]):
            nines_reached.append(position)
            return 1
        return 0
    next_trail_positions = find_next_positions(position, trail_map)
    n_trails = 0
    for next_position in next_trail_positions:
        n_trails += find_trails(next_position, trail_map, nines_reached)
    return n_trails


def solve_first_task(file):
    summ = 0
    puzzle = array([array([int(el) for el in line.strip()]) for line in file])
    zeros = where(puzzle == 0)
    zero_positions = [array([zeros[0][i], zeros[1][i]]) for i in range(len(zeros[0]))]
    for zero in zero_positions:
        nines_reached = []
        summ += find_trails(zero, puzzle, nines_reached)
    return summ


def main():
    data = open("day10/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
