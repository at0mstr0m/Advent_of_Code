raw_data = [line for line in open('Inputs/Day08Input.txt', 'r').read().splitlines()]
input_data = [[''.join(sorted(num)) for num in line.split(' ')] for line in [data.split(' | ')[0] for data in raw_data]]
for i in range(len(input_data)):
    input_data[i] = sorted(input_data[i], key=len)
output_data = [[num for num in line.split(' ')] for line in [data.split(' | ')[1] for data in raw_data]]

answer_one = 0

for line in output_data:
    for num in line:
        length = len(num)
        if length in [2, 3, 4, 7]:  # 1, 7, 4 or 8
            answer_one += 1

print(f'Answer 1: {answer_one}')  # 519


def symmetric_difference(x: str, y: str) -> str:
    return ''.join((set(x) - set(y)).union(set(y) - set(x)))


def get_0_6_9_c_d_e(line: list, one: str, four: str):
    eight = 'abcdefg'
    for i in range(len(line)):
        if len(line[i]) == 6:
            if symmetric_difference(line[i], eight) in list(one):
                six = line[i]
                c = symmetric_difference(line[i], eight)
            elif symmetric_difference(line[i], eight) in list(four):
                d = symmetric_difference(line[i], eight)
                zero = line[i]
            else:
                e = symmetric_difference(line[i], eight)
                nine = line[i]
    return zero, six, nine, c, d, e


def decode_input(line: list) -> dict[str, int]:
    assert len(line) == 10
    digits = {0: None,
              1: line[0],
              2: None,
              3: None,
              4: line[2],
              5: None,
              6: None,
              7: line[1],
              8: line[-1],
              9: None,
              }
    segments = {'a': symmetric_difference(digits[1], digits[7]),
                'b': None,
                'c': None,
                'd': None,
                'e': None,
                'f': None,
                'g': None,
                }
    digits[0], digits[6], digits[9], segments['c'], segments['d'], segments['e'] = get_0_6_9_c_d_e(line,
                                                                                                   digits[1],
                                                                                                   digits[4])
    segments['f'] = symmetric_difference(digits[1], segments['c'])
    segments['b'] = symmetric_difference(digits[4], segments['c'] + segments['d'] + segments['f'])
    segments['g'] = symmetric_difference(digits[0],
                                         segments['a'] + segments['b'] + segments['c'] + segments['e'] + segments['f'])
    digits[2] = ''.join(sorted(segments['a'] + segments['c'] + segments['d'] + segments['e'] + segments['g']))
    digits[3] = ''.join(sorted(segments['a'] + segments['c'] + segments['d'] + segments['f'] + segments['g']))
    digits[5] = ''.join(sorted(segments['a'] + segments['b'] + segments['d'] + segments['f'] + segments['g']))
    return {value: key for key, value in digits.items()}  # https://stackoverflow.com/a/483833


def decode_output(digits: dict[str, int], output: list[str]) -> int:
    result = ''
    for num in output:
        result += str(digits[''.join(sorted(list(num)))])
    return int(result)


assert len(input_data) == len(output_data)

answer_two = 0
for i in range(len(input_data)):
    answer_two += decode_output(decode_input(input_data[i]), output_data[i])

print(f'Answer 2: {answer_two}')
