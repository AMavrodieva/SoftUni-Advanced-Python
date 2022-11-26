n, m = [int(x) for x in input().split(', ')]
matrix = []
result = 0
for i in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    for j in range(m):
        result += matrix[i][j]
print(result)
print(matrix)

# Втори вариант
n, m = [int(x) for x in input().split(', ')]  # 3, 6

matrix = []

matrix_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    matrix_sum += sum(row)
print(matrix_sum)
print(matrix)