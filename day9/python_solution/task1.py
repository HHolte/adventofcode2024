
def get_blocks_and_spaces(file):
    blocks = []
    spaces = []
    for line in file:
        line = line.strip()
        for i in range(len(line)):
            if i % 2 == 0:
                blocks.append(int(line[i]))
            else:
                spaces.append(int(line[i]))
    return blocks, spaces


def solve_first_task(file):
    blocks, spaces = get_blocks_and_spaces(file)
    compact_blocks = []
    counter = 0
    block_pos_rev = len(blocks) - 1
    finished = False
    while not finished:
        if counter > block_pos_rev:
            break
        if counter == block_pos_rev:
            compact_blocks += [counter for _ in range(blocks[counter])]
            break
        compact_blocks += [counter for _ in range(blocks[counter])]
        number_of_spaces = spaces[counter]
        while number_of_spaces != 0:
            if number_of_spaces - blocks[block_pos_rev] < 0:
                compact_blocks += [block_pos_rev for _ in range(number_of_spaces)]
                blocks[block_pos_rev] -= number_of_spaces
                number_of_spaces = 0
            else:
                number_of_spaces -= blocks[block_pos_rev]
                compact_blocks += [block_pos_rev for _ in range(blocks[block_pos_rev])]
                blocks[block_pos_rev] = 0
                block_pos_rev -= 1
        counter += 1
    summ = 0
    for i in range(len(compact_blocks)):
        summ += i * compact_blocks[i]
    return summ


def main():
    data = open("day9/ex_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
