def is_outside(current_row, current_col, size):
    if current_row < 0 or current_row > size -1 or current_col < 0 or current_col > size - 1:
        return


def check_gift(number_of_present, current_row, current_col, size, directions, count_of_nice_kids):
    for direction in directions:
        next_row, next_col = directions[direction](current_row, current_col)
        if is_outside(next_row, next_col, size):
            continue
        if neighborhood[next_row][next_col] == "X":
            number_of_present -= 1
        elif neighborhood[next_row][next_col] == "V":
            count_of_nice_kids -= 1
            number_of_present -= 1
        neighborhood[next_row][next_col] = "-"
        if number_of_present == 0:
            break
    return number_of_present, count_of_nice_kids


number_of_present = int(input())
size = int(input())

directions = {
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "left": lambda r, c: (r, c - 1),
        "right": lambda r, c: (r, c + 1)
    }

neighborhood = []
santa_row, santa_col = 0, 0
count_of_nice_kids = 0

for row in range(size):
    neighborhood.append([x for x in input().split(" ")])
    for col in range(size):
        if neighborhood[row][col] == "S":
            santa_row, santa_col = row, col
        elif neighborhood[row][col] == "V":
            count_of_nice_kids += 1
target = count_of_nice_kids

while number_of_present > 0:
    command = input()
    if command == "Christmas morning":
        break
    neighborhood[santa_row][santa_col] = "-"
    next_row, next_col = directions[command](santa_row, santa_col)
    if is_outside(next_row, next_col, size):
        continue
    elif neighborhood[next_row][next_col] == "V":
        count_of_nice_kids -= 1
        number_of_present -= 1
    elif neighborhood[next_row][next_col] == "C":
        number_of_present, count_of_nice_kids = check_gift(number_of_present, next_row, next_col, size, directions, count_of_nice_kids)

    neighborhood[next_row][next_col] = "S"
    santa_row, santa_col = next_row, next_col


if number_of_present == 0 and count_of_nice_kids > 0:
    print('Santa ran out of presents!')
[print(" ".join(x)) for x in neighborhood]
if count_of_nice_kids == 0:
    print(f'Good job, Santa! {target} happy nice kid/s.')
else:
    print(f'No presents for {count_of_nice_kids} nice kid/s.')