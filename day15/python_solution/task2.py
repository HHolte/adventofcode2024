
from numpy import array, where
from task1 import cmd_to_pos, get_map_and_commands, get_sum_of_coords


def expand_map(mapp):
    new_mapp_list = []
    for row in mapp:
        new_row = []
        for el in row:
            if el == "O":
                new_row += ["[", "]"]
            elif el == "@":
                new_row += ["@", "."]
            else:
                new_row += [el, el]
        new_mapp_list.append(new_row)
    new_mapp = array([array([el for el in row]) for row in new_mapp_list])
    return new_mapp


def solve_second_task(file):
    mapp, commands = get_map_and_commands(file)
    mapp = expand_map(mapp)
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
    sum_of_coords = get_sum_of_coords(mapp, "[")
    return sum_of_coords


def main():
    data = open("day15/ex_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
