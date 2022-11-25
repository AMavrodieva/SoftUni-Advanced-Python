# number_of_name = int(input())
# unique_names = set()
# for _ in range(number_of_name):
#     name = input()
#     unique_names.add(name)
# print(*unique_names, sep='\n')

# Вариант 2
number_of_name = int(input())
unique_names = {input() for _ in range(number_of_name)}
print(*unique_names, sep='\n')
