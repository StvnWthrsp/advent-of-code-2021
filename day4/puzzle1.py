with open('input') as input:
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

def checkForWin(board_numbers, called_indexes, num):
    for i, space in enumerate(board_numbers):
        if space == num:
            # print(f"Space at index {i} contains called number {num}")
            called_indexes.append(i)

            # Check for win based on indexes
            board_index = i // 25
            row_pos = i % 5
            row_start = i - row_pos
            col_start = i - (i % 25 - row_pos)

            # print(f"X value = {i % 5}")
            # print(f"line_start = {line_start}")

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
                return board_index

# "Call" numbers and check for winner
winner = None
for num in number_sequence:
    winner = checkForWin(board_numbers, called_indexes, num)
    if winner != None:
        board_start = winner*25
        unmarked_sum = 0
        for i in range(board_start, board_start+25):
            if i not in called_indexes:
                unmarked_sum += int(board_numbers[i])
        print(f"SOLUTION = {unmarked_sum} * {num} = {int(unmarked_sum) * int(num)}")
        break
