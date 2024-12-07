from math import prod
from itertools import product


def update_result(result, value, operator):
    match operator:
        case "+":
            return result + value
        case "*":
            return result * value
        case "||":  # Relevant for task 2
            return int(str(result) + str(value))


def valid_combination_exists(value, operands, operators):
    initial_result = operands.pop(0)
    operator_combinations = list(product(operators, repeat=len(operands)))
    for combination in operator_combinations:
        result = initial_result
        for i in range(0, len(operands)):
            result = update_result(result, operands[i], combination[i])
        if result == value:
            return True
    return False


# Is possible to ditch this and just use valid_combination_exists directly
def operands_can_produce_value(value, operands, operators):
    if 1 not in operands and 0 not in operands:
        max_value = prod(operands)
        min_value = sum(operands)
        if value == min_value or value == max_value:
            return True
        if not min_value < value < max_value:
            return False
    return valid_combination_exists(value, operands, operators)


def solve_first_task(file):
    summ = 0
    operators = ["+", "*"]
    for line in file:
        test_value, operands = line.split(":")
        test_value = int(test_value)
        operands = [int(operand) for operand in operands.strip().split(" ")]
        if operands_can_produce_value(test_value, operands, operators):
            summ += test_value
    return summ


def main():
    data = open("day7/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
