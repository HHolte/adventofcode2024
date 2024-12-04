from numpy import array, fliplr


def count_xmases(string: str):
    return string.count("XMAS") + string.count("SAMX")


def solve_first_task(file):
    total_xmases = 0
    puzzle = array([array(list(line.strip())) for line in file])
    print(puzzle)
    for row in puzzle:
        total_xmases += count_xmases("".join(row))
    for col in puzzle.T:
        total_xmases += count_xmases("".join(col))
    for i in range(-puzzle.shape[0], puzzle.shape[0]):
        diag = puzzle.diagonal(i)
        anti_diag = fliplr(puzzle).diagonal(i)
        total_xmases += count_xmases("".join(diag)) + count_xmases("".join(anti_diag))
    return total_xmases


def main():
    data = open("day4/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
