data = [line for line in open(
    '2022/Inputs/Day03Input.txt', 'r').read().splitlines()]
letters = "abcdefghijklmnopqrstuvwxyz"
letters += letters.upper()
numbers = [num for num in range(1, len(letters) + 1)]
priorities = dict(zip(letters, numbers))

results = []
for i in range(len(data)):
    line = data[i]
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
    for letter in first_half:
        if second_half.find(letter) > -1:
            results.append(priorities[letter])
            break
print(f'Answer 1: {sum(results)}')

badges = []
for i in range(0, len(data), 3):
    group = data[i:i + 3]
    badge = set(group[0]) & set(group[1]) & set(group[2])
    badges.append(priorities[badge.pop()])

print(f'Answer 2: {sum(badges)}')
