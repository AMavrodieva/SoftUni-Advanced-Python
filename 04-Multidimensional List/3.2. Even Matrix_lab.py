# n = int(input())
# matrix = []
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     matrix.append([x for x in row if x % 2 == 0])
# print(matrix)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])
print([[x for x in row if x % 2 == 0]for row in matrix])

# # Вариант с Nested comprehension
# matrix = [[int(x) for x in input().split(", ")]for _ in range(int(input()))]
# print([[x for x in row if x % 2 == 0] for row in matrix])
