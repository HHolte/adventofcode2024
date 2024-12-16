import functools


def remove_trailing_zeros(stone):
    stone_without_zeros = "0"
    for i in range(len(stone)):
        if stone[i] != "0":
            stone_without_zeros = stone[i:]
            break
    return stone_without_zeros


@functools.lru_cache(10000000)
def check_stone(new_stone, n_checks):
    n_stones = 0
    if n_checks == 0:
        return 1
    if new_stone == "0":
        n_stones += check_stone("1", n_checks - 1)
    elif len(new_stone) % 2 == 0:
        n_stones += check_stone(new_stone[:len(new_stone) // 2], n_checks - 1)
        n_stones += check_stone(remove_trailing_zeros(new_stone[len(new_stone) // 2:]), n_checks - 1)
    else:
        n_stones += check_stone(str(int(new_stone) * 2024), n_checks - 1)
    return n_stones


def solve_first_task(file, n_blinks):
    stones = [stone for stone in file.readline().strip().split(" ")]
    n_stones = 0
    for stone in stones:
        n_stones += check_stone(stone, n_blinks)
    return n_stones


def main():
    data = open("day11/test_data.txt", "r")

    n_blinks = 25
    solution = solve_first_task(data, n_blinks)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
