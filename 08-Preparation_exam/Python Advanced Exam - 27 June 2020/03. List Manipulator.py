from collections import deque


def list_manipulator(*args):
    list_of_numbers = deque([int(x) for x in args[0]])
    action = args[1]
    direction = args[2]
    number = []
    for el in args[3:]:
        if el == 0:
            continue
        number.append(el)
    new_list = []
    if action == "add" and direction == 'beginning':
        if number:
            new_list.extend(number)
        new_list.extend(list_of_numbers)
    elif action == 'add' and direction == 'end':
        new_list = list_of_numbers
        if number:
            new_list.extend(number)
    elif action == 'remove' and direction == 'beginning':
        if number:
            for el in range(len(number)+1):
                list_of_numbers.popleft()
        else:
            list_of_numbers.popleft()
        new_list = list_of_numbers
    elif action == 'remove' and direction == 'end':
        if number:
            for el in range(len(number)+1):
                list_of_numbers.pop()
        else:
            list_of_numbers.pop()
        new_list = list_of_numbers

    return [*new_list]

print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))             
print(list_manipulator([1,2,3], "add", "beginning", 20))            
print(list_manipulator([1,2,3], "add", "end", 30))                  
print(list_manipulator([1,2,3], "remove", "end", 2))                
print(list_manipulator([1,2,3], "remove", "beginning", 2))          
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          
