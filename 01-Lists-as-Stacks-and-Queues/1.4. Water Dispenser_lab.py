from collections import deque
water_quantity = int(input())
command = input()
queue = deque()
while command != "Start":
    name_of_person = command
    queue.append(name_of_person)
    command = input()
while command != "End":
    if command.startswith("refill"):
        current_command, litters = command.split()
        water_quantity += int(litters)
    elif command.isdigit():
        wanted_litters = int(command)
        if water_quantity >= wanted_litters:
            print(f'{queue.popleft()} got water')
            water_quantity -= wanted_litters
        else:
            print(f'{queue.popleft()} must wait')
    command = input()
print(f'{water_quantity} liters left')
