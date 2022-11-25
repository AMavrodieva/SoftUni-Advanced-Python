from collections import deque
number_of_petrol_pumps = int(input())
pumps = deque()

for _ in range(number_of_petrol_pumps):
    pumps.append([int(x) for x in input().split()])
for attempt in range(number_of_petrol_pumps):
    current_petrol = 0
    is_attempt_failed = False
    for amount_of_petrol, distance in pumps:
        current_petrol = current_petrol + amount_of_petrol - distance
        if current_petrol < 0:
            is_attempt_failed = True
            break
    if is_attempt_failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
