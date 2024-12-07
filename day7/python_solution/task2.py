from task1 import valid_combination_exists


def solve_second_task(file):
    summ = 0
    operators = ["+", "*", "||"]
    counter = 0
    for line in file:
        test_value, operands = line.split(":")
        test_value = int(test_value)
        operands = [int(operand) for operand in operands.strip().split(" ")]
        if counter % 10 == 0:
            print("Trying line ", counter)
        if valid_combination_exists(test_value, operands, operators):
            summ += test_value
        counter += 1
    return summ


def main():
    data = open("day7/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
