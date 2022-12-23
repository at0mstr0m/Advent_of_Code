from collections import Counter

adapters = [0] + sorted([int(number) for number in open('Inputs/Day10Input.txt', 'r').read().splitlines()])
adapters.append(max(adapters) + 3)
differences = Counter([b-a for a, b in zip(adapters, adapters[1:])])
print('Answer 1:', differences[1] * differences[3])

possibilities = [1] + [0] * adapters[-1]
for i in adapters[1:]:
    possibilities[i] = possibilities[i - 1] + possibilities[i - 2] + possibilities[i - 3]
print('Answer 2:', possibilities[-1])
