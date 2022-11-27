# gifts = {
#         "Football": [100, 199],
#         "Teddy Bear": [200, 299],
#         "Lego Construction Set": [300]
#     }

def is_inside(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True


def sum_column(matrix, current_column):
    result = 0
    for ind, row in enumerate(matrix):
        result += matrix[ind][current_column]
    return result


n = 6
# matrix = [[int(x) if x.isdigit() else x for x in input().split(' ')] for row in range(n)]
board = []
list_of_trows = []
for _ in range(n):
    board.append([int(x) if x.isdigit() else x for x in input().split(' ')])

total_sum = 0
present = ""


for _ in range(3):
    current_position = input().strip("()")
    cur_row, cur_col = current_position.split(', ')
    cur_row, cur_col = int(cur_row), int(cur_col)
    if is_inside(cur_row, cur_col, n):
        if board[cur_row][cur_col] == "B":
            board[cur_row][cur_col] = 0
            total_sum += sum_column(board, cur_col)

prize = ""

if total_sum in range(100, 200):
    prize = "Football"
elif total_sum in range(200, 300):
    prize = "Teddy Bear"
elif total_sum >= 300:
    prize = "Lego Construction Set"

if total_sum < 100:
    needs_sum = 100 - total_sum
    print(f'Sorry! You need {needs_sum} points more to win a prize.')
else:
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")

