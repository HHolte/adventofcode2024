from math import floor


def parse_rules_and_updates(data):
    rules = {}
    updates = []
    for line in data:
        if line == "\n":
            continue
        line = line.strip()
        if "|" in line:
            first, second = line.split("|")
            if first not in rules:
                rules[first] = [second]
            else:
                rules[first].append(second)
        else:
            updates.append(line)
    return rules, updates


def is_update_in_correct_order(update: list[str], rules):
    for i in range(len(update) - 1):
        for sub_number in update[i + 1:]:
            if update[i] not in rules:
                return False
            if sub_number not in rules[update[i]]:
                return False
    return True


def solve_first_task(file):
    sum_middle_pages = 0
    rules, updates = parse_rules_and_updates(file)
    for update in updates:
        numbers = update.split(",")
        is_correct_order = is_update_in_correct_order(numbers, rules)
        sum_middle_pages += int(numbers[floor(len(numbers) / 2)]) if is_correct_order else 0
    return sum_middle_pages


def main():
    data = open("day5/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
