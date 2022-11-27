from collections import deque
def best_list_pureness(*args):
    list_of_number = [int(x) for x in args[0]]
    number = args[1]
    best_pureness = 0
    best_rotation = 0
    rotation = 0
    for _ in range(number+1):
        current_pureness = 0
        for ind, el in enumerate(list_of_number):
            current_sum = ind * el
            current_pureness += current_sum
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation
        list_of_number.insert(0, list_of_number.pop(-1))
        rotation += 1

    return f'Best pureness {best_pureness} after {best_rotation} rotations'

# sum_value = sum([(number * index) for number, index in enumerate(sequence)])

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
