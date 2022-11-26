# def create_2x2_matrix(matrix, row, col):
#     creator = {
#         0: [matrix[row][col], matrix[row][col + 1]],
#         1: [matrix[row + 1][col], matrix[row + 1][col + 1]]
#     }
#     n = len(creator)
#     new_matrix = []
#     for r in range(n):
#         new_matrix.append(creator[r])
#     return new_matrix
#
#
#
# def check_symbols(new_matrix):
#     r = 0
#     c = 0
#     searched_symbol = ''
#     searched_symbol = new_matrix[r][c]
#     if searched_symbol == new_matrix[r][c+1]:
#         if searched_symbol == new_matrix[r+1][c]:
#             if searched_symbol == new_matrix[r+1][c+1]:
#                 return True
#
#
# n, m = [int(x) for x in input().split()]
# matrix = []
# for _ in range(n):
#     matrix.append(input().split())
# searched_symbol = ''
# count_symbol = 0
# for row in range(n):
#     for col in range(m):
#         if 0 <= row + 1 < n and 0 <= col + 1 < m:
#             new_matrix = create_2x2_matrix(matrix, row, col)
#             if check_symbols(new_matrix):
#                 count_symbol += 1
# print(count_symbol)

# Решение на упражнението
n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append(input().split())

count_symbol = 0

for row in range(n-1):
    for col in range(m-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            count_symbol += 1
print(count_symbol)