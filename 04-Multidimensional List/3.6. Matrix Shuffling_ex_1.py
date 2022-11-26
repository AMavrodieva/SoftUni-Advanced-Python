def is_valid(command, rows, columns):
    row_1, col_1, row_2, col_2 = [int(x) for x in command[1:]]
    if row_1 < 0 or row_1 >= rows or col_1 < 0 or col_1 >= columns:
        return False
    if row_2 < 0 or row_2 >= rows or col_2 < 0 or col_2 >= columns:
        return False
    return True


rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    if not is_valid(command, rows, columns):
        print("Invalid input!")
        continue
    row_1, col_1, row_2, col_2 = [int(x) for x in command[1:]]
    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
    for row in matrix:
        print(*row, sep=" ")
