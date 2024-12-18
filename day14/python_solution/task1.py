from math import prod


class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def __init__(self, line):
        pos, vel = line.strip().split(" ")
        self.position = tuple(int(p) for p in pos.split("=")[1].split(","))
        self.velocity = tuple(int(v) for v in vel.split("=")[1].split(","))

    def update_position(self, number_of_updates, map_width, map_height):
        new_pos_x = (self.position[0] + self.velocity[0] * number_of_updates) % map_width
        new_pos_y = (self.position[1] + self.velocity[1] * number_of_updates) % map_height
        self.position = (new_pos_x, new_pos_y)


def get_quadrant(position, map_width, map_height):
    if position[0] == int(map_width / 2) or position[1] == int(map_height / 2):
        return 0
    if position[0] < map_width / 2:
        if position[1] < map_height / 2:
            return 1
        return 3
    if position[1] < map_height / 2:
        return 2
    return 4


def solve_first_task(file):
    map_width = 101
    map_height = 103
    seconds = 100
    positions = []
    for line in file:
        robot = Robot(line)
        robot.update_position(seconds, map_width, map_height)
        positions.append(robot.position)
    quadrants = [get_quadrant(pos, map_width, map_height) for pos in positions]
    possible_quadrants = [1, 2, 3, 4]
    product = prod([quadrants.count(el) for el in possible_quadrants if el != 0])
    return product


def main():
    data = open("day14/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
