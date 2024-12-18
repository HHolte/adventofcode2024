from numpy import zeros, printoptions, inf
from task1 import Robot


# Had to look this one up, apparently most of the robots form a picture of a Christmas tree when all robots
# are in a unique position...
def solve_second_task(file):
    map_width = 101
    map_height = 103
    robots: list[Robot] = []
    for line in file:
        robots.append(Robot(line))
    all_robots_in_unique_positions = len(set([robot.position for robot in robots])) == len(robots)
    seconds_elapsed = 0
    while not all_robots_in_unique_positions:
        for robot in robots:
            robot.update_position(1, map_width, map_height)
        all_robots_in_unique_positions = len(set([robot.position for robot in robots])) == len(robots)
        seconds_elapsed += 1

    # Print to behold the masterpiece
    grid = zeros([map_width, map_height])
    for robot in robots:
        grid[robot.position] += 1
    with printoptions(threshold=inf):
        print(grid.T)

    return seconds_elapsed


def main():
    data = open("day14/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
