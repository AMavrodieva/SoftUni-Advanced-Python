size = int(input())
field = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split(" ")
    for col in range(size):
        if row_elements[col] == 'B':
            bunny_row = row
            bunny_col = col
    field.append(row_elements)

best_sum = float('-inf')
best_direction = ""
best_path = []


directions = {
        "up": lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1)
    }
for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    current_path = []
    while 0 <= row < size and 0 <= col < size and field[row][col] != "X":
        current_sum += int(field[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)
    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep='\n')
print(best_sum)
