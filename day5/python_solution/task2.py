from functools import cmp_to_key
from math import floor
from task1 import is_update_in_correct_order, parse_rules_and_updates


def sort_and_get_middle_page(update: list[str], rules):
    def compare(a, b):
        if a in rules:
            if b in rules[a]:
                return 1
        return -1
    sorted_update = sorted(update, key=cmp_to_key(compare))
    return int(sorted_update[floor(len(update) / 2)])


def solve_second_task(file):
    sum_middle_pages = 0
    rules, updates = parse_rules_and_updates(file)
    for update in updates:
        numbers = update.split(",")
        is_correct_order = is_update_in_correct_order(numbers, rules)
        if not is_correct_order:
            sum_middle_pages += sort_and_get_middle_page(numbers, rules)
    return sum_middle_pages


def main():
    data = open("day5/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
