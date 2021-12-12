import numpy as np

data = np.array([int(num) for num in open('Inputs/Day07Input.txt', 'r').read().split(',')])
calculate_consumption = np.vectorize(lambda x: np.sum(np.arange(x + 1)))

minimum = np.min(data)
maximum = np.max(data)

consumption_record = []
real_consumption_record = []

for level in range(minimum, maximum + 1):   # try every level
    consumption = np.absolute(data - np.full(shape=data.shape, fill_value=level))
    consumption_record.append(np.sum(consumption))
    real_consumption_record.append(np.sum(calculate_consumption(consumption)))

print(f'Answer 1: {min(consumption_record)}')
print(f'Answer 2: {min(real_consumption_record)}')
