class ValueCannotBeNegative(Exception):
    pass


for num in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative

# Решение лекция
class ValueCannotBeNegative(Exception):
    pass


values = [int(input()) for _ in range(5)]

for value in values:
    if value < 0:
        raise ValueCannotBeNegative(f'{value} should be >= 0')