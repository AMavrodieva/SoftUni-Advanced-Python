def is_valid(current_row, current_col, size):
    if 0 <= current_row < size and 0 <= current_col < size:
        return True


def get_next_step(direction, current_row, current_col, size):
    if direction == "up":
        return current_row - 1, current_col
    elif direction == "down":
        return current_row + 1, current_col
    elif direction == "left":
        return current_row, current_col - 1
    elif direction == 'right':
        return current_row, current_col + 1



size = int(input())
board = []
snake_row, snake_col = 0, 0
burrow_position = []
for row in range(size):
    board.append([x for x in input()])
    for col in range(size):
        if board[row][col] == 'S':
            snake_row, snake_col = row, col
        if board[row][col] == "B":
            burrow_position.append((row, col))

food = 0
is_loss = False
while not is_loss and food < 10:
    direction = input()
    board[snake_row][snake_col] = '.'
    next_row, next_col = get_next_step(direction, snake_row, snake_col, size)
    if not is_valid(next_row, next_col, size):
       is_loss = True
       break
    if board[next_row][next_col] == "*":
        food += 1
        snake_row, snake_col = next_row, next_col
    elif board[next_row][next_col] == "B":
        board[next_row][next_col] = "."
        if burrow_position[0] == board[next_row][next_col]:
            other_row, other_col = burrow_position[0]
            snake_row, snake_col = other_row, other_col
        else:
            other_row, other_col = burrow_position[1]
            snake_row, snake_col = other_row, other_col
    else:
        snake_row, snake_col = next_row, next_col

if is_loss:
    print(f'Game over!')
else:
    board[snake_row][snake_col] = "S"
    print(f'You won! You fed the snake.')
print(f'Food eaten: {food}')
[print("".join(x for x in row)) for row in board]
