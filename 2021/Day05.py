import numpy as np

data = np.array([[[int(coordinate) for coordinate in coordinates.split(',')]
                  for coordinates in line.split(' -> ')]
                 for line in open('Inputs/Day05Input.txt', 'r').read().splitlines()])
diagram = np.zeros((1000, 1000))
for i in range(len(data)):
    x1 = data[i, 0, 0]
    x2 = data[i, 1, 0]
    y1 = data[i, 0, 1]
    y2 = data[i, 1, 1]
    if x1 == x2:
        if y1 < y2:
            diagram[y1: y2 + 1, x1] += 1
        elif y1 > y2:
            diagram[y2: y1 + 1, x1] += 1
    elif y1 == y2:
        if x1 < x2:
            diagram[y1, x1: x2 + 1] += 1
        elif x1 > x2:
            diagram[y1, x2: x1 + 1] += 1
answer_one = 0
for iy, ix in np.ndindex(diagram.shape):
    if diagram[iy, ix] > 1:
        answer_one += 1
print(f'Answer 1: {answer_one}')
for i in range(len(data)):
    x1 = data[i, 0, 0]
    x2 = data[i, 1, 0]
    y1 = data[i, 0, 1]
    y2 = data[i, 1, 1]
    if x1 != x2 and y1 != y2:
        diagonal_length = abs(abs(y2) - abs(y1)) + 1
        if x1 > x2 and y1 > y2:
            for j in range(diagonal_length):
                diagram[y1 - j, x1 - j] += 1
        elif x1 > x2:
            for j in range(diagonal_length):
                diagram[y1 + j, x1 - j] += 1
        elif y1 > y2:
            for j in range(diagonal_length):
                diagram[y1 - j, x1 + j] += 1
        else:
            for j in range(diagonal_length):
                diagram[y1 + j, x1 + j] += 1
answer_two = 0
for iy, ix in np.ndindex(diagram.shape):
    if diagram[iy, ix] > 1:
        answer_two += 1
print(f'Answer 2: {answer_two}')
