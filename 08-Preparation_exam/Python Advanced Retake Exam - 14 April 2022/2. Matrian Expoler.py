def get_direction(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def is_valid_coordinate(current_row, current_col, n):
    if 0 <= current_row < n and 0 <= current_col < n:
        return True
    return False


def goes_out_of_filed(current_row, current_col, n):
    if current_row < 0:
        return n-1, current_col
    elif current_row >= n:
        return 0, current_col
    if current_col < 0:
        return current_row, n-1
    elif current_col >= n-1:
        return current_row, 0


n = 6
matrix =[]
current_row = 0
current_col = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "E":
            current_row, current_col = row, col
command_list = [command for command in input().split(', ')]


water_deposit = False
metal_deposit = False
concrete_deposit = False

for command in command_list:
    current_row, current_col = get_direction(command, current_row, current_col)
    if not is_valid_coordinate(current_row, current_col, n):
        current_row, current_col = goes_out_of_filed(current_row, current_col, n)
    if matrix[current_row][current_col] == "W":
        water_deposit = True
        print(f'Water deposit found at ({current_row}, {current_col})')
    elif matrix[current_row][current_col] == "M":
        metal_deposit = True
        print(f'Metal deposit found at ({current_row}, {current_col})')
    elif matrix[current_row][current_col] == "C":
        concrete_deposit = True
        print(f'Concrete deposit found at ({current_row}, {current_col})')
    elif matrix[current_row][current_col] == "R":
        print(f'Rover got broken at ({current_row}, {current_col})')
        break

if water_deposit and metal_deposit and concrete_deposit:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
