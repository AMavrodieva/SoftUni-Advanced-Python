def get_next_positions(row, col, directions):
    if directions == 'up':
        return row - 1, col
    if directions == 'down':
        return row + 1, col
    if directions == 'left':
        return row, col - 1
    if directions == 'right':
        return row, col + 1


def goes_outside(player_row, player_col, n, m):
    if 0 <= player_row < n and 0 <= player_col < m:
        return False
    return True


def get_traverse_field(player_row, player_col, n, m):
    if player_row < 0:
        return n-1, player_col
    elif player_row >= n:
        return 0, player_col

    if player_col < 0:
        return player_row, m-1
    elif player_col >= m-1:
        return player_row, 0


n, m = [int(x) for x in input().split(', ')]
player = "Y"
player_row, player_col = 0, 0
santa_workshop = []
target_cell = 0
for row in range(n):
    santa_workshop.append(input().split(" "))
    for col in range(m):
        cell_value = santa_workshop[row][col]
        if cell_value == "Y":
            player_row, player_col = row, col
        elif cell_value == "D" or cell_value == "G" or cell_value == "C":
            target_cell += 1


christmas_decoration = 0
gift = 0
cookies = 0
player = "Y"
is_successful = False


while target_cell != 0:
    command = input()
    if command == "End":
        santa_workshop[player_row][player_col] = "Y"
        break
    direction, steps = command.split('-')
    steps = int(steps)
    for step in range(steps):
        if target_cell == 0:
            break
        santa_workshop[player_row][player_col] = "x"
        player_row, player_col = get_next_positions(player_row, player_col, direction)
        if goes_outside(player_row, player_col, n, m):
            if target_cell != 0:
                player_row, player_col = get_traverse_field(player_row, player_col, n, m)
            else:
                break
        cell_value = santa_workshop[player_row][player_col]
        if cell_value == "D":
            christmas_decoration += 1
            target_cell -= 1
        elif cell_value == "G":
            gift += 1
            target_cell -= 1
        elif cell_value == "C":
            cookies += 1
            target_cell -= 1
        santa_workshop[player_row][player_col] = "Y"
    santa_workshop[player_row][player_col] = "Y"


if target_cell == 0:
    print(f'Merry Christmas!')
print(f"You've collected:")
print(f'- {christmas_decoration} Christmas decorations')
print(f'- {gift} Gifts')
print(f'- {cookies} Cookies')
for row in santa_workshop:
    print(*row)
