
def solve_first_task(file):
    blocks = []
    spaces = []
    checksum = 0
    for block_pos, el in enumerate(file.readline().strip()):
        if block_pos % 2 == 0:
            blocks.append(el)
        else:
            spaces.append(el)
    space_pos = 0
    for block_pos in range(len(blocks) - 1, 0, -1):
        block = blocks[block_pos]
        while block > 0:
            space = spaces[space_pos]
            if block > space:
                block -= space
                space[space_pos] = 0
                space_pos += 1
            else:
                space[space_pos] -= block
                block = 0
                # Update block position somehow

    return checksum


def main():
    data = open("day9/ex_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
