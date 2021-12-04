import numpy as np

raw_data = [line for line in open('Inputs/Day04Input.txt', 'r').read().splitlines() if line != '']
lucky_numbers = [int(num) for num in raw_data.pop(0).split(',')]
boards = []
for i in range(0, len(raw_data), 5):
    board = []
    for j in range(i, i + 5):
        board.append([[int(num), False] for num in raw_data[j].split(' ') if num != ''])
    boards.append(board)
boards = np.array(boards)
for draw in lucky_numbers:
    first_winning_board, first_final_draw = None, None
    for i in range(len(boards)):  # iterate boards
        for j in range(5):  # iterate rows
            for k in range(5):  # iterate columns
                if boards[i][j][k][0] == draw:
                    boards[i][j][k][1] = True
    # check for a winner
    for i in range(len(boards)):  # iterate boards
        for j in range(5):  # iterate rows and columns
            if np.sum(boards[i, j, :, 1]) == 5 or np.sum(boards[i, :, j, 1]) == 5:
                first_winning_board, first_final_draw = i, draw
    if first_winning_board and first_final_draw:
        break
first_winning_board = boards[first_winning_board]
result_one = 0
for i in range(5):  # iterate rows
    for j in range(5):  # iterate columns
        if np.sum(first_winning_board[i, j, 1]) == 0:
            result_one += first_winning_board[i, j, 0]
print(f'Answer 1: {result_one * first_final_draw}')
winner_list = []
final_draw = None
for draw in lucky_numbers:
    for i in range(len(boards)):  # iterate boards
        if i in winner_list:        # ignore boards, that already won
            continue
        for j in range(5):  # iterate rows
            for k in range(5):  # iterate columns
                if boards[i][j][k][0] == draw:
                    boards[i][j][k][1] = True
    # check for a winner
    for i in range(len(boards)):  # iterate boards
        if i in winner_list:
            continue
        for j in range(5):  # iterate rows and columns
            if np.sum(boards[i, j, :, 1]) == 5 or np.sum(boards[i, :, j, 1]) == 5:
                winner_list.append(i)
                final_draw = draw
last_winner = boards[winner_list.pop()]
result_two = 0
for i in range(5):  # iterate rows
    for j in range(5):  # iterate columns
        if np.sum(last_winner[i, j, 1]) == 0:
            result_two += last_winner[i, j, 0]

print(f'Answer 2: {result_two * final_draw}')
