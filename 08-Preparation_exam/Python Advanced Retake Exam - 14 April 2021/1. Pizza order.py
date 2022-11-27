from collections import deque


def is_order_valid(pizza_orders, current_order):
    if 0 < current_order <= 10 and len(pizza_orders) >= 0:
        return current_order
    if not pizza_orders:
        return None
    return is_order_valid(pizza_orders, pizza_orders.popleft())


def is_valid(employees_capacities, current_employee):
    if current_employee > 0 and len(employees_capacities) >= 0:
        return current_employee
    if not employees_capacities:
        return None
    return is_valid(employees_capacities, employees_capacities.pop())


pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacities = [int(y) for y in input().split(", ")]

count_of_pizza = 0

while pizza_orders and employees_capacities:
    order_to_validate = pizza_orders.popleft()
    current_order = is_order_valid(pizza_orders, order_to_validate)
    if not current_order:
        break
    employee_to_validate = employees_capacities.pop()
    current_employee = is_valid(employees_capacities, employee_to_validate)
    if not current_employee:
        pizza_orders.append(current_order)
        break
    if current_employee >= current_order:
        count_of_pizza += current_order
    else:
        current_order -= current_employee
        count_of_pizza += current_employee
        pizza_orders.appendleft(current_order)


if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {count_of_pizza}')
    if employees_capacities:
        print(f'Employees: {", ".join([str(x) for x in employees_capacities])}')
else:
    print(f'Not all orders are completed.')
    if pizza_orders:
        print(f'Orders left: {", ".join([str(y) for y in pizza_orders])}')
