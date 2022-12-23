data = [line for line in open('2022/Inputs/Day01Input.txt', 'r').read().splitlines()]
elves = []
elf = []
for line in data:
    if line == '':
        elves.append(sum(elf))
        elf = []
        continue
    elf.append(int(line))
answer_one = elves[elves.index(max(elves))]
print(f'Answer 1: {answer_one}')
answer_two = 0
for i in range(3):
    answer_two += elves.pop(elves.index(max(elves)))
print(f'Answer 2: {answer_two}')
