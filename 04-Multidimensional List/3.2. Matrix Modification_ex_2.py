n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
command = input()
while command != 'END':
    current_command = command.split()[0]
    row, col, value = [int(x) for x in command.split()[1:]]
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
        print(f'Invalid coordinates')
        command = input()
        continue
    if current_command == "Add":
        matrix[row][col] += value
    if current_command == "Subtract":
        matrix[row][col] -= value
    command = input()
[print(' '.join([str(x) for x in row]))for row in matrix]
# for row in matrix:
#     print(*row, sep=' ')