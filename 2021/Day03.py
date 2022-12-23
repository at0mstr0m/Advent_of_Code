import numpy as np

data_array = np.array([[int(num) for num in list(binary)]
                       for binary in open('Inputs/Day03Input.txt', 'r').read().splitlines()])
gamma_rate = ""
for column in range(data_array.shape[1]):
    # which bit apears the most can easily be determined by the rounded mean of each column
    gamma_rate += str(int(np.around(np.mean(data_array[:, column]))))
epsilon_rate = ''.join(['0' if num == '1' else '1' for num in list(gamma_rate)])
print(f'Answer 1: {int(gamma_rate, base=2) * int(epsilon_rate, base=2)}')

oxygen_data_array = data_array.copy()
co2_data_array = data_array.copy()
for column in range(data_array.shape[1]):
    oxygen_zeros = np.count_nonzero(oxygen_data_array[:, column] == 0)
    oxygen_ones = np.count_nonzero(oxygen_data_array[:, column] == 1)
    co2_zeros = np.count_nonzero(co2_data_array[:, column] == 0)
    co2_ones = np.count_nonzero(co2_data_array[:, column] == 1)
    most_appearing_bit = 1 if oxygen_zeros <= oxygen_ones else 0
    least_appearing_bit = 1 if co2_zeros <= co2_ones else 0
    # basically implements .pop() for a np.array using a list comprehension
    oxygen_data_array = np.array([row for row in oxygen_data_array.tolist() if row[column] == most_appearing_bit])
    co2_data_array = np.array([row for row in co2_data_array.tolist() if row[column] == least_appearing_bit])

oxygen_generator_rating = int(''.join(str(bit) for bit in oxygen_data_array[0].tolist()),
                              base=2)
co2_scrubber_rating = int(''.join(str(bit) for bit in co2_data_array[0].tolist()),
                          base=2)

print(f'oxygen_generator_rating = {oxygen_generator_rating}')       # 1177
print(f'co2_scrubber_rating = {co2_scrubber_rating}')               # 4070
print(f'Answer 2: {oxygen_generator_rating * co2_scrubber_rating}') # 4790390
