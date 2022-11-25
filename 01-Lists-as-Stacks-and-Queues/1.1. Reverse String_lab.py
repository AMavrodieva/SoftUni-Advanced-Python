string = list(input())
reversed_str = []
for el in range(len(string)):
    reversed_str.append(string.pop())
print("".join(reversed_str))


