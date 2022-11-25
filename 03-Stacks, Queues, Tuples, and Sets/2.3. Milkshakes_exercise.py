from collections import deque

chocolates = [int(x) for x in input().split(',')]
cups_of_milk = deque([int(x) for x in input().split(',')])
milkshakes = 0
while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    if current_milk == current_chocolate:
        milkshakes += 1
    else:
        cups_of_milk.append(current_milk)
        chocolates.append(current_chocolate - 5)
if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')
if cups_of_milk:
    print(f'Milk: {", ".join([str(x) for x in cups_of_milk])}')
else:
    print(f'Milk: empty')
