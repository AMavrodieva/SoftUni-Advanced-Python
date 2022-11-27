def is_inside(current_row, current_col, n):
    if 0 <= current_row < n and 0 <= current_col < n:
        return True


def get_next_steps(direction, current_row, current_col):
    directions = {
        "up":  (current_row - 1, current_col),
        "down":  (current_row + 1, current_col),
        "left": (current_row, current_col - 1),
        "right":  (current_row, current_col + 1)
    }

    next_row, next_col = directions[direction]

    return next_row, next_col


initial_string = input()
size = int(input())
matrix = []
player_row, player_col = 0, 0

for row in range(size):
    current_row = [x for x in input()]
    for col in range(size):
        if current_row[col] == "P":
            player_row, player_col = row, col
    matrix.append(current_row)

for _ in range(int(input())):
    direction = input()
    next_row, next_col = get_next_steps(direction, player_row, player_col)
    if is_inside(next_row, next_col, size):
        if matrix[next_row][next_col] == "-":
            pass
        else:
            initial_string += matrix[next_row][next_col]
        matrix[next_row][next_col] = 'P'
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_row, next_col
    else:
        if initial_string:
            initial_string = initial_string[0:len(initial_string) - 1]


print(initial_string)
[print("".join(x)) for x in matrix]
