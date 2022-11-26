def is_valid(current_row, current_col, size):
    if 0 <= current_row < size and 0 <= current_col < size:
        return True


def positions(row, col, directions):
    if directions == 'up':
        return row - 1, col
    elif directions == 'down':
        return row + 1, col
    elif directions == 'left':
        return row, col - 1
    elif directions == 'right':
        return row, col + 1


size = int(input())
board = []
alice_row = 0
alice_col = 0
for row in range(size):
    row_element = input().split(" ")
    for col in range(size):
        if row_element[col] == "A":
            alice_row = row
            alice_col = col
    board.append(row_element)



count_of_tea_bags = 0
while count_of_tea_bags < 10:
    board[alice_row][alice_col] = "*"
    command = input()
    next_row, next_col = positions(alice_row, alice_col, command)
    if not is_valid(next_row, next_col, size):
        break
    alice_row, alice_col = next_row, next_col
    if board[alice_row][alice_col] == "." or board[next_row][next_col] == "*":
        continue
    if board[alice_row][alice_col] == "R":
        break

    count_of_tea_bags += int(board[next_row][next_col])


board[alice_row][alice_col] = "*"

if count_of_tea_bags >= 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")

for row in board:
    print(*row, sep=" ")

