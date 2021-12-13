import numpy as np

data = np.array([[int(num) for num in list(line)] for line in open('Inputs/Day09Input.txt', 'r').read().splitlines()])
print(data)
print(data.shape)


def compare_up(a: int, b: int) -> bool:
    return data[b, a] < data[b + 1, a]


def compare_down(a: int, b: int) -> bool:
    return data[b, a] < data[b - 1, a]


def compare_right(a: int, b: int) -> bool:
    return data[b, a] < data[b, a + 1]


def compare_left(a: int, b: int) -> bool:
    return data[b, a] < data[b, a - 1]

answer_one = 0
for y, x in np.ndindex(data.shape):
    try:
        if compare_up(x, y) and compare_left(x, y) and compare_right(x, y) and compare_down(x, y):  # around
            answer_one += data[y, x] + 1
    except IndexError:
        try:
            if compare_left(x, y) and compare_right(x, y) and compare_down(x, y):                   # L, R, D
                answer_one += data[y, x] + 1
        except IndexError:
            try:
                if compare_up(x, y) and compare_right(x, y) and compare_down(x, y):                 # U, R, D
                    answer_one += data[y, x] + 1
            except IndexError:
                try:
                    if compare_up(x, y) and compare_left(x, y) and compare_down(x, y):              # U, L, D
                        answer_one += data[y, x] + 1
                except IndexError:
                    try:
                        if compare_up(x, y) and compare_left(x, y) and compare_right(x, y):         # R, L, U
                            answer_one += data[y, x] + 1
                    except IndexError:
                        try:
                            if compare_up(x, y) and compare_left(x, y):                             # U, L
                                answer_one += data[y, x] + 1
                        except IndexError:
                            try:
                                if compare_left(x, y) and compare_down(x, y):                       # L, D
                                    answer_one += data[y, x] + 1
                            except IndexError:
                                try:
                                    if compare_right(x, y) and compare_down(x, y):                   # R, D
                                        answer_one += data[y, x] + 1
                                except IndexError:
                                    try:
                                        if compare_right(x, y) and compare_up(x, y):                 # R, U
                                            answer_one += data[y, x] + 1
                                    except IndexError:
                                        print(f'Fatal error at x={x} and y={y}')
                                        break

print(f'Answer 1: {answer_one}')
