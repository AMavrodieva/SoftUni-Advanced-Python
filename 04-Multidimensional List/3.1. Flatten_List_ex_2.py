elements = [x for x in input().split('|')]
result = []
for index in range(len(elements)-1, -1, -1):
    current_element = elements[index].split()
    result.extend(current_element)

print(' '.join(result))

# Решение на лекцията
elements = [x for x in input().split('|')]
result = []
for index in range(len(elements)-1, -1, -1):
    current_element = elements[index].strip().split()
    result.extend(current_element)

print(' '.join(result))
