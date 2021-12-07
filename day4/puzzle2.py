with open('/home/steven/advent-of-code-2021/day4/input') as input:
    lines = input.readlines()

number_sequence = lines[0].split(',')
board_numbers = []
called_indexes = []

# Flatten data structure for boards
for i, line in enumerate(lines):
    if i == 0:
        continue
    if line == '\n':
        continue
    stripped_line = line.strip('\n')
    num_list = line.split()
    for num in num_list:
        board_numbers.append(num)

def checkForWin(board_numbers, called_indexes, num, score_map):
    winners = []
    for i, space in enumerate(board_numbers):
        if space == num:
            called_indexes.append(i)

            # If board has already won, skip it
            board_index = i // 25
            if board_index in score_map.keys():
                continue

            # Check for win based on indexes
            row_pos = i % 5
            row_start = i - row_pos
            col_start = i - (i % 25 - row_pos)

            horizontal_win = True
            for j in range(row_start, row_start+5):
                if j not in called_indexes:
                    horizontal_win = False

            vertical_win = True
            for j in range(col_start, col_start+25, 5):
                if j not in called_indexes:
                    vertical_win = False
                    
            if horizontal_win or vertical_win:
                print(f"Winner on board {board_index}")
                winners.append(board_index)
    
    return winners

score_map = {}
last_winner = -1

for num in number_sequence:
    winners = None
    winners = checkForWin(board_numbers, called_indexes, num, score_map)
    if winners:
        for board in winners:
            if board in score_map.keys():
                continue
            last_winner = board
            board_start = board*25
            unmarked_sum = 0
            for i in range(board_start, board_start+25):
                if i not in called_indexes:
                    unmarked_sum += int(board_numbers[i])
            score_map[board] = int(unmarked_sum) * int(num)

print(last_winner)
print(score_map[last_winner])