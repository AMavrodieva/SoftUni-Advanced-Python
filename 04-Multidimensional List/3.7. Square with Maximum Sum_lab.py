def find_new_matrix(matrix, row, col):
    rows_generator = {
        0: [matrix[row][col], matrix[row][col + 1]],
        1: [matrix[row + 1][col], matrix[row + 1][col + 1]]
    }
    new_matrix = []
    for row in range(len(rows_generator)):
        element = rows_generator[row]
        new_matrix.append(element)
    return new_matrix


def sum_new_matrix(new_matrix):
    result = 0
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix)):
            result += new_matrix[i][j]
    return result


n, m = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")]for _ in range(n)]
best_matrix_sum = 0
best_matrix = []

for row in range(n):
    for col in range(m):
        if 0 <= row + 1 < n and 0 <= col + 1 < m:
            new_matrix = find_new_matrix(matrix, row, col)
            current_sum = sum_new_matrix(new_matrix)
            if current_sum > best_matrix_sum:
                best_matrix_sum = current_sum
                best_matrix = new_matrix

print(*best_matrix[0])
print(*best_matrix[1])
print(best_matrix_sum)
