data = [int(number) for number in open('Inputs/Day01Input.txt', 'r').read().splitlines()]
answer_one = sum(data[i] < data[i + 1] for i in range(len(data) - 1))
print(f'Answer 1: {answer_one}')
three_measurement = [data[i] + data[i + 1] + data[i + 2] for i in range(len(data) - 2)]
answer_two = sum(three_measurement[i] < three_measurement[i + 1] for i in range(len(three_measurement) - 1))
print(f'Answer 2: {answer_two}')
