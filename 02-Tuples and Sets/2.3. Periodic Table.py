# number = int(input())
# chemical_elements = set()
# elements = sum([input().split() for _ in range(number)], [])
# for el in elements:
#     chemical_elements.add(el)
# print(*chemical_elements, sep='\n')

# Втори вариант
# n = int(input())
# ch_element = set()
# for _ in range(n):
#     result = set(input().split())
#     ch_element = ch_element.union(result)
# print(*ch_element, sep='\n')

# Трети вариант
m = int(input())
element = set()
for _ in range(m):
    element = element.union(set(input().split()))
print(*element, sep='\n')


