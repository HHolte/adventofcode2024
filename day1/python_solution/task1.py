from sys import argv


def solve_first_task(file):
    list_of_first_numbers = []
    list_of_second_numbers = []
    for line in file:
        first_number, second_number = line.split()
        list_of_first_numbers.append(int(first_number.strip()))
        list_of_second_numbers.append(int(second_number.strip()))
    list_of_first_numbers.sort()
    list_of_second_numbers.sort()
    return sum([abs(list_of_first_numbers[i] - list_of_second_numbers[i]) for i in range(len(list_of_first_numbers))])


def main():
    test_or_ex = argv[1]
    data = open(f"day1/{test_or_ex}_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
