data = open('2022/Inputs/Day06Input.txt', 'r').read()

def find_distinct_chars(s, length):
    for i, _ in enumerate(s):
        if len(set(data[i:i + length])) == length:
            return i + length
    return -1

print(f'Answer 1: {find_distinct_chars(data, 4)}')
print(f'Answer 2: {find_distinct_chars(data, 14)}')
