numbers = input().split()
reversed_stack = []

while numbers:
    reversed_stack.append(numbers.pop())
print(*reversed_stack, end=' ')
