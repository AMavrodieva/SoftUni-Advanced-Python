from collections import deque
expression = input().split()
numbers = deque()
evaluator = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b
}
for character in expression:
    if character in evaluator:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            result = evaluator[character](first_number, second_number)
            numbers.appendleft(result)
    else:
            numbers.append(int(character))
print(*numbers)
