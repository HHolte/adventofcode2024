from task1 import solve_first_task


def solve_second_task(file):
    n_blinks = 75
    return solve_first_task(file, n_blinks)


def main():
    data = open("day11/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
