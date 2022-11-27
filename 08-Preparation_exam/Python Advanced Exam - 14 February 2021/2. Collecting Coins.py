from math import floor


def get_next_step(direction, current_row, current_col):
    row, col = directions[direction](current_row, current_col)
    return row, col


def is_outside(current_row, current_col, n):
    if current_row < 0 or current_row > n-1 or current_col < 0 or current_col > n-1:
        return True


def traverse_field(matrix, n, next_row, next_col):
    if next_row < 0:
        return n-1, next_col
    elif next_row > n-1:
        return 0, next_col
    if next_col < 0:
        return next_row, n-1
    elif next_col > n-1:
        return  next_row, 0


n = int(input())
player_row = 0
player_col = 0
matrix = []
coins = 0
for row in range(n):
    matrix.append([int(x) if x.isdigit() else x for x in input().split(" ")])
    for col in range(n):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

directions = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1)
}

path = []
while coins < 100:
    direction = input()
    if direction not in directions:
        continue
    path.append((player_row, player_col))
    matrix[player_row][player_col] = 0
    next_row, next_col = get_next_step(direction, player_row, player_col)
    if is_outside(next_row, next_col, n):
        next_row, next_col = traverse_field(matrix, n, next_row, next_col)
    # path.append((next_row, next_col))
    if matrix[next_row][next_col] == "X":
        coins = floor(coins/2)
        player_row, player_col = next_row, next_col
        break
    coins += matrix[next_row][next_col]
    player_row, player_col = next_row, next_col

path.append((player_row, player_col))
if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print(f"Your path:")
[print(f'[{row}, {col}]') for row, col in path]

