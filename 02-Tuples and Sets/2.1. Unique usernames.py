# n = int(input())
# unique_usernames = set()
# for _ in range(n):
#     usernames = input()
#     unique_usernames.add(usernames)
# print(*unique_usernames, sep='\n')

# Вариант 2
n = int(input())
unique_usernames = {input() for _ in range(n)}
[print(el) for el in unique_usernames]

