# n = int(input())
# matrix = [input() for _ in range(n)]
# symbol = input()
# is_found_symbol = False
# for row in range(n):
#     for col in range(n):
#         if symbol == matrix[row][col]:
#             is_found_symbol = True
#             print(f'({row}, {col})')
#             break
#     if is_found_symbol:
#         break
#
# if not is_found_symbol:
#     print(f'{symbol} does not occur in the matrix')

# Второ решение
n = int(input())
matrix = [input() for _ in range(n)]
symbol = input()
is_found_symbol = False
for row in range(n):
    if symbol in matrix[row]:
        col = matrix[row].index(symbol)
        is_found_symbol = True
        print(f'({row}, {col})')
        break
if not is_found_symbol:
    print(f'{symbol} does not occur in the matrix')


# Решение на лекцията
# def find_symbol(matrix, symbol):
#     # for row_index in range(n):
#     #     for column_index in range(n):
#     #         if matrix[row_index][column_index] == symbol:
#     #             return row_index, column_index
#
#     for row_index in range(n):
#         if symbol in matrix[row_index]:
#             column_index = matrix[row_index].index(symbol)
#             return row_index, column_index
#
#
# n = int(input())
#
# matrix = [list(input()) for _ in range(n)]
# symbol = input()
#
# result = find_symbol(matrix, symbol)
#
# if result:
#     row_index, column_index = result
#     print(f'({row_index}, {column_index})')
# else:
#     print(f'{symbol} does not occur in the matrix')



