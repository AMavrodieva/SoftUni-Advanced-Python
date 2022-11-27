def is_valid(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True


def check_queen(row, col, n):
    is_find = False
    for direction in directions:
        queen_row, queen_col = row, col
        if is_find:
            break
        while True:
            next_row, next_col = directions[direction](queen_row, queen_col)
            if not is_valid(next_row, next_col, n):
                break
            elif chess_board[next_row][next_col] == "Q":
                break
            elif chess_board[next_row][next_col] == "K":
                is_find = True
                break
            else:
                queen_row, queen_col = next_row, next_col
    if is_find:
        return True


n = 8
chess_board = [input().split(" ") for _ in range(n)]
queen_capture = []
directions = {
    "horizontally_left": lambda r, c: (r, c-1),
    "horizontally_right": lambda r, c: (r, c+1),
    "vertically_up_": lambda r, c: (r-1, c),
    "vertically_down": lambda r, c: (r+1, c),
    "diagonally_up_left": lambda r, c: (r-1, c-1),
    "diagonally_down_left": lambda r, c: (r+1, c-1),
    "diagonally_up_right": lambda r, c: (r-1, c+1),
    "diagonally_down_right": lambda r, c: (r+1, c+1),
}

for ind_row, row in enumerate(chess_board):
    if "Q" in row:
        for col in range(n):
            if chess_board[ind_row][col] == "Q":
                if check_queen(ind_row, col, n):
                    queen_capture.append((ind_row, col))
                    continue
if len(queen_capture) > 0:
    for el in queen_capture:
        print(f'[{el[0]}, {el[1]}]')
else:
    print(f"The king is safe!")

# if queen_capture:
#     print(*queen_capture, sep='\n')