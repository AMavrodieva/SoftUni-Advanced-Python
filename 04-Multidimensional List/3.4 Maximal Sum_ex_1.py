from sys import maxsize


def is_matched_matrix(matrix, row, col):
    new_matrix = []
    r = row
    c = col
    for row in range(3):
        rows = [matrix[r][c], matrix[r][c+1], matrix[r][c+2]]
        new_matrix.append(rows)
        r += 1
    return new_matrix


def sum_matrix(new_matrix):
    n = len(new_matrix)
    result = 0
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix)):
            result += new_matrix[i][j]
    return result


n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()]for _ in range(n)]
max_sum = - maxsize
matched_matrix = []


for row in range(n-2):
    for col in range(m-2):
        current_matrix = is_matched_matrix(matrix, row, col)
        current_sum = sum_matrix(current_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            matched_matrix = current_matrix
print(f'Sum = {max_sum}')
[print(*row) for row in matched_matrix]
