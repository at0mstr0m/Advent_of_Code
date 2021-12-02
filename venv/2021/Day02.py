data = [line.split(' ') for line in open('Inputs/Day02Input.txt', 'r').read().splitlines()]
horizontal = 0
depth = 0
for command, x in data:
    x = int(x)
    if command == 'forward':
        depth += x
    elif command == 'down':
        horizontal += x
    elif command == 'up':
        horizontal -= x

print(f'Answer 1: {horizontal * depth}')

horizontal = 0
depth = 0
aim = 0
for command, x in data:
    x = int(x)
    if command == 'forward':
        horizontal += x
        depth += aim * x
    elif command == 'down':
        aim += x
    elif command == 'up':
        aim -= x

print(f'Answer 2: {horizontal * depth}')
