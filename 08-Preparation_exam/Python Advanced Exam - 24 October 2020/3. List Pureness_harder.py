def best_list_pureness(*args):
    list_of_number = [int(x) for x in args[0]]
    number = args[1]
    result = ""
    best_pureness = 0
    rotation = 0
    pareness_dict = {}
    for _ in range(number+1):
        current_pureness = 0
        for ind, el in enumerate(list_of_number):
            current_sum = ind * el
            current_pureness += current_sum
        if current_pureness not in pareness_dict:
            pareness_dict[current_pureness] = []
        pareness_dict[current_pureness].append(rotation)
        if current_pureness > best_pureness:
            best_pureness = current_pureness
        list_of_number.insert(0, list_of_number.pop(-1))
        rotation += 1


    for key, value in pareness_dict.items():
        if key == best_pureness:
            result = f'Best pureness {key} after {value[0]} rotations'
            break
    return result


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
