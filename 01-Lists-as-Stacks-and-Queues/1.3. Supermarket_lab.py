from collections import deque
command = input()
queue = deque()
count = 0
while command != "End":
    if command != "Paid":
        queue.append(command)
        count += 1
    else:
        while queue:
            print(queue.popleft())
        queue = deque()
        count = 0
    command = input()
print(f'{count} people remaining.')