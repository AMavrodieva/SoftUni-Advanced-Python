def is_need_rest(rest):
    if rest > 0:
        return True


def play_game(current_row, current_col, n, player, rest):
    win_player = ""
    if board[current_row][current_col] == "E":
        win_player = first_player if player == 1 else second_player
        print(f'{win_player} found the Exit and wins the game!')
        player = None
        return player, current_row, current_col, rest
    elif board[current_row][current_col] == "T":
        loss_player = first_player if player == 1 else second_player
        win_player = second_player if loss_player == first_player else first_player
        print(f"{loss_player} is out of the game! The winner is {win_player}.")
        player = None
        return player, current_row, current_col, rest
    elif board[current_row][current_col] == "W":
        rest += 1
        rest_player = first_player if player == 1 else second_player
        print(f'{rest_player} hits a wall and needs to rest.')
        return player, current_row, current_col, rest
    else:
        return player, current_row, current_col, rest


first_player, second_player = input().split(", ")
n = 6
board = []
for _ in range(n):
    board.append([str(x) for x in input().split(" ")])

current_pl_row, current_pl_col = 0, 0
other_pl_row, other_pl_col = 0, 0
current_player = 1
other_player = 2


turn = 0
rest_pl_1 = 0
rest_pl_2 = 0
while True:
    position = input().strip("()").split(", ")
    input_row, input_col = int(position[0]), int(position[1])
    turn += 1
    if turn % 2 == 1:
        if is_need_rest(rest_pl_1):
            rest_pl_1 -= 1
            continue
        current_player, current_pl_row, current_pl_col, rest_pl_1 = play_game(input_row, input_col, n, current_player, rest_pl_1)
        if current_player is None:
            break
    else:
        if is_need_rest(rest_pl_2):
            rest_pl_2 -= 1
            continue
        other_player, other_pl_row, other_pl_col, rest_pl_2 = play_game(input_row, input_col, n, other_player, rest_pl_2)
        if other_player is None:
            break

