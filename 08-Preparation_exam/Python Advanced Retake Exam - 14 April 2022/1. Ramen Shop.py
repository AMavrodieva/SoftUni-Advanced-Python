from collections import deque
bows_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(y) for y in input().split(', ')])

while bows_of_ramen and customers:
    current_ramen = bows_of_ramen.pop()
    current_customer = customers.popleft()
    if current_ramen == current_customer:
        continue
    if current_ramen > current_customer:
        current_ramen -= current_customer
        bows_of_ramen.append(current_ramen)

    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)


if not customers:
    print(f'Great job! You served all the customers.')
    if bows_of_ramen:
        print(f'Bowls of ramen left: {", ".join([str(x) for x in bows_of_ramen])}')
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
