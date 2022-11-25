given_numbers = [float(x) for x in input().split()]
numbers = {}
for number in given_numbers:
    if number not in numbers:
        numbers[number] = 0
    numbers[number] += 1
for number, count in numbers.items():
    print(f'{number:.1f} - {count} times')
