from collections import defaultdict

with open('Inputs\Day05input.txt', 'r') as f:
    seatings = f.read().split('\n')
seat_IDs = []
decoded_seatings = defaultdict(list)

def row_approximation(i:int, letter:str) -> int:
    if letter == 'B':
        return 2**(6-i)
    return 0

def column_approximation(i:int, letter:str) -> int:
    if letter == 'R':
        return 2**(2-i)
    return 0

def calculate_seat_id(row:int, column:int) -> int:
    return (row * 8) + column

for seating in seatings:
    row = 0
    column = 0
    min_row = 0
    max_row = 127
    for i in range(7):                                      # first 7 letters provide row
        row += row_approximation(i, seating[i])
    for j in range(7,10):
        column += column_approximation((j-7), seating[j])   # last 3 letters provide column
    seat_IDs.append(calculate_seat_id(row, column))
    decoded_seatings[row].append(column)

print('Answer 1:', max(seat_IDs))

my_row = 0
my_column = 0

# find out my_row
for key in decoded_seatings:
    if len(decoded_seatings[key]) != 8:
        if key > 3 and key < 123:               # exclude first and last rows
            my_row = key

# find out my_column
for i in range(8):                              # checks which seat in the row is not taken
    if i not in decoded_seatings[my_row]:
        my_column = i

print('Answer 2:', calculate_seat_id(my_row, my_column))