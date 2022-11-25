number_1, number_2 = [int(x) for x in input().split()]
first_set = {int(input()) for _ in range(number_1)}
second_set = {int(input()) for _ in range(number_2)}
number_in_both_sets = first_set.intersection(second_set)
[print(number) for number in number_in_both_sets]

# Втори вариант
n, m = [int(x) for x in input().split()]

first = set()
second = set()
for _ in range(n):
    first.add(int(input()))
for _ in range(m):
    second.add((int(input())))
result = first.intersection(second)
for num in result:
    print(num)
