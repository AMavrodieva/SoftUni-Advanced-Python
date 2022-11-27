from collections import deque
males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])

matches = 0

while males and females:
    current_male = males.pop()
    if current_male <= 0:
        continue
    elif current_male % 25 == 0:
        males.pop()
        continue
    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue
    elif current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_male != current_female:
        current_male -= 2
        males.append(current_male)
    else:
        matches += 1

print(f'Matches: {matches}')
if males:
    males = males[::-1]
    print(f'Males left: {", ".join([str(x) for x in males])}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print(f'Females left: none')



