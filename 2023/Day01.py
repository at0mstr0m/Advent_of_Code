import re

raw_data = open('2023/Inputs/Day01Input.txt', 'r').read().splitlines()

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

int_pattern = re.compile(r'[0-9]')
all_number_pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))')

def find_first_and_last_digit(line: str, pattern: re.Pattern):
    digits = [numbers[digit] if digit in numbers.keys() else digit for digit in re.findall(pattern, line)]
    return int(''.join([digits[0], digits[-1]]))

answer_one = sum([find_first_and_last_digit(line, int_pattern) for line in raw_data])

print(f'Answer 1: {answer_one}')

answer_two = sum([find_first_and_last_digit(line, all_number_pattern) for line in raw_data])

print(f'Answer 2: {answer_two}')

print(find_first_and_last_digit('one1two2three3four4five5six6seven7eight8nine9', all_number_pattern))
