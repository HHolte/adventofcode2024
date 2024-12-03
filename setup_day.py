from os import makedirs
from sys import argv
from data_downloader import download_and_save_data, get_file_name


def write_task_content(day: int, task: int):
    task_str = "first" if task == 1 else "second"
    return (
        f"""
            def solve_{task_str}_task(file):
                pass


            def main():
                data = open("day{day}/ex_data.txt", "r")

                solution = solve_{task_str}_task(data)
                print("Solution {task_str} task: ", solution)

                data.close()


            if __name__ == "__main__":
                main()
            """
    )


def setup_task_file(day, task):
    file_name = "task1.py" if task == 1 else "task2.py"
    content = write_task_content(day, task) if task == 1 else write_task_content(day, task)
    task1_file = open(f"day{day}/python_solution/{file_name}", "w+")
    task1_file.write(content)
    task1_file.close()


def setup_folders_and_files(day: int):
    makedirs(f"day{day}/python_solution", exist_ok=True)
    setup_task_file(day, 1)
    setup_task_file(day, 2)
    open(get_file_name(day, "ex_data"), "w+").close()


def main():
    day = int(argv[1])
    year = 2024
    setup_folders_and_files(day)
    download_and_save_data(day, year)


if __name__ == "__main__":
    main()
