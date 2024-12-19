from numpy import array, where

cmd_to_pos = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def get_map_and_commands(file):
    map_lines = []
    commands = ""
    for line in file:
        if line == "\n":
            break
        map_lines.append(line.strip())
    mapp = array([array([el for el in line]) for line in map_lines])
    for line in file:
        commands += line.strip()
    return mapp, commands


def get_sum_of_coords(mapp, box_char):
    boxes = where(mapp == box_char)
    gps = [boxes[0][i] * 100 + boxes[1][i] for i in range(len(boxes[0]))]
    return sum(gps)


def solve_first_task(file):
    mapp, commands = get_map_and_commands(file)
    robot_pos = tuple(ind[0] for ind in where(mapp == "@"))
    mapp[robot_pos] = "."
    for cmd in commands:
        pos_change = cmd_to_pos[cmd]
        new_pos = (robot_pos[0] + pos_change[0], robot_pos[1] + pos_change[1])
        element_at_new_pos = mapp[new_pos]
        if element_at_new_pos == ".":
            robot_pos = new_pos
            continue
        if element_at_new_pos == "#":
            continue
        try_pos = new_pos
        while True:
            next_pos = (try_pos[0] + pos_change[0], try_pos[1] + pos_change[1])
            if mapp[next_pos] == ".":
                mapp[next_pos] = "O"
                mapp[new_pos] = "."
                robot_pos = new_pos
                break
            if mapp[next_pos] == "#":
                break
            try_pos = next_pos
    sum_of_coords = get_sum_of_coords(mapp, "O")
    return sum_of_coords


def main():
    data = open("day15/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
