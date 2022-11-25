from collections import deque
quantity_of_food = int(input())
quantity_of_each_order = [int(x) for x in input().split()]
orders = deque(quantity_of_each_order)
print(max(orders))
is_complete = False
while orders:
    current_order = orders.popleft()
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
        is_complete = True
    else:
        is_complete = False
        orders.appendleft(current_order)
        break
left_order = [str(x) for x in orders]
if is_complete:
    print(f'Orders complete')
else:
    print(f'Orders left: {" ".join(left_order)} ')