n = int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]
primary_diagonal = [matrix[i][j] for j in range(len(matrix)) for i in range(len(matrix)) if i == j]
secondary_diagonal = [matrix[i][j] for j in range(len(matrix)) for i in range(len(matrix)) if j == n - i -1]

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in reversed(secondary_diagonal)])}. Sum: {sum(secondary_diagonal)}')
