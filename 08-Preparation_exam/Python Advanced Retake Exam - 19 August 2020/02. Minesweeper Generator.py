def is_valid(current_row, current_col, n):
    if 0 <= current_row < n and 0 <= current_col < n:
        return True


def check_bombs(current_row, current_col, n, directions):
    count_bombs = 0
    for direction in directions:
        row, col = current_row, current_col
        next_row, next_col = directions[direction](row, col)
        if is_valid(next_row, next_col, n):
            if board[next_row][next_col] == "*":
                count_bombs += 1
    if count_bombs > 0:
        return count_bombs
    return None


size = int(input())
bombs_nums = int(input())
directions = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1),
    "up_left": lambda r, c: (r-1, c-1),
    "up_right": lambda r, c: (r-1, c+1),
    "down_left": lambda r, c: (r+1, c-1),
    'down_right': lambda r, c: (r+1, c+1)
}
board = []
for row in range(size):
    row_element = [None] * size
    board.append(row_element)

for x in range(bombs_nums):
    current_position = input().strip("()")
    current_row, current_col = current_position.split(", ")
    current_row, current_col = int(current_row), int(current_col)
    if is_valid(current_row, current_col, size):
        board[current_row].pop(current_col)
        board[current_row].insert(current_col, '*')


for ind_row, row in enumerate(board):
    for ind_col, col in enumerate(board):
        if board[ind_row][ind_col] != "*":
            count = check_bombs(ind_row, ind_col, size, directions)
            if count is not None:
                board[ind_row].pop(ind_col)
                board[ind_row].insert(ind_col, count)
            else:
                board[ind_row].pop(ind_col)
                board[ind_row].insert(ind_col, 0)


[print(" ".join([str(x) for x in row])) for row in board]

