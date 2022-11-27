def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))

    return (None, None)


def get_name_position(row, col):
    row_name = [8, 7, 6, 5, 4, 3, 2, 1]
    col_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return row_name[row], col_name[col]


n = 8
board = [input().split() for _ in range(n)]

is_queen = False
is_capture = False
current_delta = - 1
other_delta = + 1
current_player = 'w'
other_player = "b"
current_position = find_player_position(board, 'w')
other_position = find_player_position(board, 'b')

while not is_capture and not is_queen:
    (current_row, current_col) = current_position
    (other_row, other_col) = other_position
    current_row += current_delta
    current_position = (current_row, current_col)
    if current_row == other_row and abs(current_col - other_col) == 1:
        is_capture = True
        current_position = (current_row, other_col)
    elif current_row in (0, n - 1):
        is_queen = True
        current_position = (current_row, current_col)
    else:
        current_position, other_position = other_position, current_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player

player = "White" if current_player == 'w' else "Black"
(row_player, col_player) = get_name_position(*current_position)
position = f'{col_player}{row_player}'

if is_capture:
    print(f'Game over! {player} win, capture on {position}.')
if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {position}.')