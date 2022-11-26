def sum_primary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))


def sum_secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n-i-1] for i in range(n))


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
difference = abs(sum_primary_diagonal(matrix) - sum_secondary_diagonal(matrix))
print(difference)