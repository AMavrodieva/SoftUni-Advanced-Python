n = int(input())
row = 1
odd_set = set()
even_set = set()
for _ in range(n):
    name = input()
    sum_characters = int(sum([ord(ch)for ch in name]) / row)
    if sum_characters % 2 == 0:
        even_set.add(sum_characters)
    else:
        odd_set.add(sum_characters)
    row += 1
if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)
print(', '.join([str(x) for x in result]))
#print(*result, sep=', ')