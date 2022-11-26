def generate_matrix(row, col, alphabetic):
    generate_row = []
    rows = {}
    for i in range(row):
        for j in range(column):
            if i in alphabetic and j in alphabetic:
                if i not in rows:
                    rows[i] = []
                rows[i].append((alphabetic[i]+alphabetic[i+j]+alphabetic[i]))
    return rows


row, column = [int(x) for x in input().split()]

alphabetic = {}
number = 97
for i in range(0, 26):
    if i not in alphabetic:
        alphabetic[i] = 0
    alphabetic[i] = chr(number)
    number += 1
current_matrix = generate_matrix(row, column, alphabetic)

for key, value in current_matrix.items():
    print(*value, sep=" ")

# Решение на лекция
row, column = [int(x) for x in input().split()]
for i in range(row):
    for j in range(column):
        print(f'{chr(97+i)}{chr(97+i+j)}{chr(97+i)}', end=" ")
    print()

#Решение 2

def generate_matrix(row, col):
    rows = {}
    for i in range(row):
        for j in range(column):
            if i not in rows:
                rows[i] = []
            rows[i].append((chr(97+i)+chr(97+i+j)+chr(97+i)))
    return rows


row, column = [int(x) for x in input().split()]

current_matrix = generate_matrix(row, column)

for key, value in current_matrix.items():
    print(*value, sep=" ")