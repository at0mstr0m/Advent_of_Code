data = [[[int(num)
          for num in sections.split('-')]
         for sections in elves.split(',')]
        for elves in open(
    '2022/Inputs/Day04Input.txt', 'r').read().splitlines()]

counter = 0
for pair in data:
    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
        counter += 1

print(f'Answer 1: {counter}')

counter = 0
for pair in data:
    pair = sorted((pair[0], pair[1]))
    if not pair[0][1] < pair[1][0]:
        counter += 1

print(f'Answer 2: {counter}')

