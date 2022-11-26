n, m = [int(x) for x in input().split(', ')]
matrix = []
sum_of_columns = [0] * m
for i in range(n):
    matrix.append([int(x) for x in input().split()])
    for j in range(m):
        sum_of_columns[j] += matrix[i][j]
print(*sum_of_columns, sep='\n')

# Решение на лекцията
# import sys
# from io import StringIO
#
# test_input1 = '''3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# '''
#
# test_input2 = '''3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
#
#
# # sys.stdin = StringIO(test_input1)
# # sys.stdin = StringIO(test_input2)
#
# def get_column_sums(matrix):
#     column_sums = [0] * columns_count
#
#     for row_index in range(rows_count):
#         for column_index in range(columns_count):
#             column_sums[column_index] += matrix[row_index][column_index]
#
#     return column_sums
#
#
# def get_column_sums2(matrix):
#     column_sums = []
#     for column_index in range(columns_count):
#         column_sums.append(0)
#         for row_index in range(rows_count):
#             column_sums[-1] += matrix[row_index][column_index]
#
#     return column_sums
#
#
# # n, m
# rows_count, columns_count = [int(x) for x in input().split(', ')]
#
# matrix = []
#
# for _ in range(rows_count):
#     matrix.append(
#         [int(x) for x in input().split(' ')]
#     )
#
# [print(x) for x in get_column_sums(matrix)]
# # [print(x) for x in get_column_sums2(matrix)]
