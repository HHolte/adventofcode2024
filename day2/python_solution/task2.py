def is_safe(diffs: list[int], can_remove: bool):
    neagtives = [diff for diff in diffs if diff < 0]
    positives = [diff for diff in diffs if diff > 0]
    if len(neagtives) >= 2 and len(positives) >= 2:
        return False
    most_negative = len(neagtives) > len(positives)
    diffs = [(-1) * diff for diff in diffs] if most_negative else diffs
    for i in range(len(diffs)):
        if (not 0 < abs(diffs[i]) <= 3) or diffs[i] < 0:
            if not can_remove:
                return False
            elif 0 < i < len(diffs) - 1:
                diffs[i - 1] += diffs[i]
            diffs.pop(i)
            return is_safe(diffs, False) if can_remove else False
    return True


def is_safe2(diffs: list[int]):
    same_sign = all(el > 0 for el in diffs) or all(el < 0 for el in diffs)
    changes_gradually = all(0 < abs(el) <= 3 for el in diffs)
    return same_sign and changes_gradually


def solve_second_task(file):
    safe_reports = 0
    for line in file:
        numbers = line.split()
        diffs = [int(numbers[i]) - int(numbers[i - 1]) for i in range(1, len(numbers))]
        # safe_reports += is_safe(diffs, True)
        if is_safe2(diffs):
            safe_reports += 1
            continue
        for i in range(len(diffs)):
            diffs_temp = diffs[:i] + diffs[i+1:]
            if i == len(diffs) - 1:
                if is_safe2(diffs_temp):
                    safe_reports += 1
                    break
            if i != 0:
                diffs_temp[i - 1] += diffs[i]
            if is_safe2(diffs_temp):
                safe_reports += 1
                break
    return safe_reports


def main():
    data = open("day2/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
