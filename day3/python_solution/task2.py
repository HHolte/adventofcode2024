from task1 import sum_muls


def solve_second_task(file):
    summ = 0
    whole_string = ""
    for line in file:
        whole_string += line.strip()
    whole_string = 'x' + whole_string
    donts = whole_string.split("don't()")
    summ += sum_muls(donts[0])
    for dont in donts[1:]:
        dos = dont.split("do()")
        summ += sum(sum_muls(do) for do in dos[1:])
    return summ


def main():
    data = open("day3/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
