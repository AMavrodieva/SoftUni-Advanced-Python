def is_outside(current_row, current_col, n):
    if current_row < 0 or current_row > n - 1 or current_col < 0 or current_col > n - 1:
        return True
    return False


def moves(board, current_row, current_col, n):
    ver_sum = 0
    for direction in directions_ver:
        row, col = directions_ver[direction](current_row, current_col)
        while not is_outside(row, col, n):
            if not str(board[row][col]).isalpha():
                ver_sum += board[row][col]
            row, col = directions_ver[direction](row, col)

    hor_sum = 0
    for direction in directions_hor:
        row, col = directions_hor[direction](current_row, current_col)
        while not is_outside(row, col, n):
            if not str(board[row][col]).isalpha():
                hor_sum += board[row][col]
            row, col = directions_hor[direction](row, col)
    return ver_sum + hor_sum


def get_score(board, n, current_row, current_col):
    result = 0
    if board[current_row][current_col] == "D":
        result = moves(board, current_row, current_col, n)
        return result * 2
    elif board[current_row][current_col] == "T":
        result = moves(board, current_row, current_col, n)
        return result * 3
    elif board[current_row][current_col] == "B":
        return 501
    else:
        result = board[current_row][current_col]
        return result


first_player, second_player = input().split(", ")
n = 7
board = []
for _ in range(n):
    row_element = [int(x) if x.isdigit() else x for x in input().split(" ")]
    board.append(row_element)

player_1_score = 501
player_2_score = 501
pl_1_throws, pl_2_throws = 0, 0

throws_count = 0
is_win_game = False
directions_ver = {
    'vertical_up': lambda r, c: (r - 1, c),
    'vertical_down': lambda r, c: (r + 1, c),
}
directions_hor = {
    'horizontal_left': lambda r, c: (r, c - 1),
    'horizontal_right': lambda r, c: (r, c + 1)
}

while True:
    if is_win_game:
        break
    current_row, current_col = input().strip("()").split(", ")
    current_row, current_col = int(current_row), int(current_col)
    throws_count += 1
    if throws_count % 2 == 1:
        pl_1_throws += 1
        if is_outside(current_row, current_col, n):
            continue
        current_score = get_score(board, n, current_row, current_col)
        player_1_score -= current_score
        if player_1_score <= 0:
            is_win_game = True
    else:
        pl_2_throws += 1
        if is_outside(current_row, current_col, n):
            continue
        current_score = get_score(board, n, current_row, current_col)
        player_2_score -= current_score
        if player_2_score <= 0:
            is_win_game = True


player = first_player if player_1_score <= 0 else second_player
trows = pl_1_throws if player_1_score <= 0 else pl_2_throws
print(f'{player} won the game with {trows} throws!')
