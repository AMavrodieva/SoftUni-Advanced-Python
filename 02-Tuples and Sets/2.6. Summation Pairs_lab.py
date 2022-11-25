from itertools import combinations
numbers = [int(x) for x in input().split()]
target_number = int(input())
unique_pairs = set()
iterations = 0
for first, second in combinations(numbers, 2):
    if first + second == target_number:
        iterations += 1
        unique_pairs.add((first, second))
        print(f'{first} + {second} = {target_number}')
    else:
        iterations += 1
print(f'Iterations done: {iterations}')
for nums in unique_pairs:
    print(f"{nums}")


