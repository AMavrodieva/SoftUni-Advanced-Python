from collections import deque
working_bees = deque([int(x) for x in input().split()])
count_of_nectar = [int(x) for x in input().split()]
symbol = deque(input().split())
total_honey = 0
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while working_bees and count_of_nectar:
    bee = working_bees.popleft()
    nectar = count_of_nectar.pop()
    if nectar < bee:
        working_bees.appendleft(bee)
        continue
    if nectar == 0:
        continue
    operator = symbol.popleft()
    total_honey += abs(operations[operator](bee, nectar))
print(f'Total honey made: {total_honey}')
if working_bees:
    print(f'Bees left: {", ".join([str(x) for x in working_bees])}')
if count_of_nectar:
    print(f'Nectar left: {", ".join([str(x) for x in count_of_nectar])}')
