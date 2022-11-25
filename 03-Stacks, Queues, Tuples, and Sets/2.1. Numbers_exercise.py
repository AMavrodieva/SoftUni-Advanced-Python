first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    current_command = command[0]
    used_set = command[1]
    if current_command == 'Add' or current_command == "Remove":
        additional_set = set([int(x) for x in command[2:]])
        if current_command == "Add" and used_set == "First":
            first_set = first_set.union(additional_set)
        if current_command == "Add" and used_set == "Second":
            second_set = second_set.union(additional_set)
        if current_command == "Remove" and used_set == "First":
            first_set = first_set.difference(additional_set)
        if current_command == "Remove" and used_set == "Second":
            second_set = second_set.difference(additional_set)
    elif current_command == "Check":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')


