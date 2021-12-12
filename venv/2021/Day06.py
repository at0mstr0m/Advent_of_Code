from collections import Counter

raw_data = [int(num) for num in open('Inputs/Day06Input.txt', 'r').read().split(',')]

raw_data = dict(Counter(raw_data))
raw_data[0] = 0
raw_data[6] = 0
raw_data[7] = 0
raw_data[8] = 0
raw_data = [[k, v] for k, v in raw_data.items()]
raw_data = sorted(raw_data, key=lambda tup: tup[0])

for day in range(256):     # 256 days
    if day == 80:
        result = 0
        for i in range(9):
            result += raw_data[i][1]
        print(f'Answer 1: {result}')
    new_0 = raw_data[1][1]
    new_1 = raw_data[2][1]
    new_2 = raw_data[3][1]
    new_3 = raw_data[4][1]
    new_4 = raw_data[5][1]
    new_5 = raw_data[6][1]
    new_6 = raw_data[7][1]
    new_7 = raw_data[8][1]
    new_8 = raw_data[0][1]
    new_6 += raw_data[0][1]
    raw_data[0][1] = new_0
    raw_data[1][1] = new_1
    raw_data[2][1] = new_2
    raw_data[3][1] = new_3
    raw_data[4][1] = new_4
    raw_data[5][1] = new_5
    raw_data[6][1] = new_6
    raw_data[7][1] = new_7
    raw_data[8][1] = new_8

result = 0
for i in range(9):
    result += raw_data[i][1]
print(f'Answer 2: {result}')
