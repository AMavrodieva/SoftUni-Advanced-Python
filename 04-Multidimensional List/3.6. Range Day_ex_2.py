def is_valid_position(current_row, current_col, size):
    if 0 <= current_row < size and 0 <= current_col < size:
        return True


def get_next_step(direction, current_row, current_col, steps):
    if direction == "up":
        return current_row - steps, current_col
    elif direction == "down":
        return current_row + steps, current_col
    elif direction == "left":
        return current_row, current_col - steps
    elif direction == 'right':
        return current_row, current_col + steps


size = 5
player_row, player_col = 0, 0
matrix = []
target = 0
shot_target = []
for row in range(size):
    matrix.append([x for x in input().split(" ")])
    for col in range(size):
        if matrix[row][col] == "A":
            player_row, player_col = row, col
        if matrix[row][col] == "x":
            target += 1

matrix[player_row][player_col] = "."
number = int(input())

for _ in range(number):
    command = input().split(" ")
    if command[0] == "move":
        current_command, direction, steps = command
        steps = int(steps)
        next_row, next_col = get_next_step(direction, player_row, player_col, steps)
        if is_valid_position(next_row, next_col, size) and matrix[next_row][next_col] == ".":
            player_row, player_col = next_row, next_col

    else:
        direction = command[1]
        pl_row, pl_col = get_next_step(direction, player_row, player_col, 1)
        while is_valid_position(pl_row, pl_col, size):
            if matrix[pl_row][pl_col] == "x":
                target -= 1
                shot_target.append([pl_row, pl_col])
                matrix[pl_row][pl_col] = "."
                break
            pl_row, pl_col = get_next_step(direction, pl_row, pl_col, 1)
        if target == 0:
            break

if target == 0:
    print(f'Training completed! All {len(shot_target)} targets hit.')
else:
    print(f'Training not completed! {target} targets left.')
print(*shot_target, sep="\n")
