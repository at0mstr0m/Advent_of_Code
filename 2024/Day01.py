from collections import Counter

raw_data = open('2024/Inputs/Day01Input.txt', 'r').read().splitlines()
pairs = [[int(n) for n in x.split('   ')] for x in raw_data]
left = sorted([pair[0] for pair in pairs])
right = sorted([pair[1] for pair in pairs])
result = []
for i in range(len(left)):
    result.append(abs(left[i] - right[i]))
print(f'Answer 1: {sum(result)}')
occurrences = Counter(right)
print(f'Answer 2: {sum([n * (occurrences.get(n) or 0) for n in left])}')