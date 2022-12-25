import re

commands = [line for line in open(
    '2022/Inputs/Day07Input.txt', 'r').read().splitlines()]
directories = {
    '/': {},
}
pwd = []


def get_folder(folders: dict, path: list):
    if not path:
        return folders
    return get_folder(folders[path[0]], path[1:] or False)


for i, command in enumerate(commands):
    if command == '$ ls':
        continue
    match = re.search(r'(\d+)\s(.+)', command)
    if re.match(r'\$ cd', command):
        destination = re.match(r'\$\scd\s(.*)', command).group(1)
        if destination == '..':
            pwd = pwd[:-1]
        else:
            pwd.append(destination)
    elif command[:3] == 'dir':
        get_folder(directories, pwd)[command[4:]] = {}
    elif match:
        get_folder(directories, pwd)[match.group(2)] = int(match.group(1))

answer_one = 0


def calc_sum(directory):
    if not isinstance(directory, dict):
        return directory
    total = sum(calc_sum(v) for v in directory.values())
    directory['SUMME'] = total
    if total < 100000:
        global answer_one
        answer_one += total
    return total


used_space = calc_sum(directories)
must_free = used_space - 40_000_000
print(f'Answer 1: {answer_one}')

answer_two = 99999999999999999


def iterate(directory):
    for key, value in directory.items():
        if isinstance(value, dict):
            iterate(value)
        else:
            global must_free
            global answer_two
            if value >= must_free and value < answer_two:
                answer_two = value


iterate(directories)
print(f'Answer 2: {answer_two}')
