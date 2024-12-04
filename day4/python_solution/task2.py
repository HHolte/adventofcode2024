from numpy import array


def is_x_mas(puzzle, row_index: int, col_index: int):
    top_left_element = puzzle[row_index - 1, col_index - 1]
    top_right_element = puzzle[row_index - 1, col_index + 1]
    bottom_left_element = puzzle[row_index + 1, col_index - 1]
    bottom_right_element = puzzle[row_index + 1, col_index + 1]
    diag_is_mas = (top_left_element == 'M' and bottom_right_element == 'S') or (top_left_element == 'S' and bottom_right_element == 'M')
    anti_diag_is_mas = (bottom_left_element == 'M' and top_right_element == 'S') or (bottom_left_element == 'S' and top_right_element == 'M')
    return diag_is_mas and anti_diag_is_mas


def solve_second_task(file):
    total_x_mases = 0
    puzzle = array([array(list(line.strip())) for line in file])
    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            el = puzzle[i, j]
            if el == "A":
                total_x_mases += is_x_mas(puzzle, i, j)
    return total_x_mases


def main():
    data = open("day4/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
