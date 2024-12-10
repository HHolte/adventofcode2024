
from task1 import get_blocks_and_spaces


def solve_second_task(file):
    blocks, spaces = get_blocks_and_spaces(file)
    compact_blocks = []
    counter = 0
    block_pos_rev = len(blocks) - 1
    finished = False
    for i in range(len(spaces)):
        compact_blocks += [i for _ in range(blocks[i])]
        space = spaces[i]
        to_remove = []
        for j in range(block_pos_rev, i, -1):
            if space == 0:
                break
            if blocks[j] <= space:
                compact_blocks += [j for _ in range(blocks[j])]
                space -= blocks[j]
                to_remove.append(j)
                

    for block in blocks.reverse():
        for space in spaces:
            if space >= block:
                pass

    while not finished:
        if counter > block_pos_rev:
            break
        if counter == block_pos_rev:
            compact_blocks += [counter for _ in range(blocks[counter])]
            break
        compact_blocks += [counter for _ in range(blocks[counter])]
        number_of_spaces = spaces[counter]
        while number_of_spaces != 0:
            if number_of_spaces < blocks[block_pos_rev]:
                block_pos_rev -= 1
            else:
                number_of_spaces -= blocks[block_pos_rev]
                compact_blocks += [block_pos_rev for _ in range(blocks[block_pos_rev])]
                blocks[block_pos_rev] = 0
                block_pos_rev -= 1
        counter += 1
    print(compact_blocks)
    summ = 0
    for i in range(len(compact_blocks)):
        summ += i * compact_blocks[i]
    return summ


def main():
    data = open("day9/ex_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
