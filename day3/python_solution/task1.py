def sum_muls(line: str):
    line = "x" + line
    mul_ends = line.split("mul(")
    line_sum = 0
    for mul_end in mul_ends[1:]:
        factors = mul_end.split(")")[0].split(",")
        two_numeric_factors = len(factors) == 2 and all([factor.isnumeric() for factor in factors])
        line_sum += int(factors[0]) * int(factors[1]) if two_numeric_factors else 0
    return line_sum


def solve_first_task(file):
    summ = 0
    for line in file:
        summ += sum_muls(line)
    return summ


def main():
    data = open("day3/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
