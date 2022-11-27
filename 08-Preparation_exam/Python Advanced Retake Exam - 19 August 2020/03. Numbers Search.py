def numbers_searching(*args):
    list_of_number = [int(x) for x in args]
    min_number = min(list_of_number)
    max_number = max(list_of_number)
    dictionary = {num: 0 for num in range(min_number, max_number+1)}
    for el in list_of_number:
        if el in dictionary:
            dictionary[el] += 1
    missing_number = 0
    duplicate = []
    for num, value in dictionary.items():
        if value == 0:
            missing_number = num
        if value > 1:
            duplicate.append(num)
    sorted_duplicate = sorted(duplicate)
    result = [missing_number, [*sorted_duplicate]]
    return result

 # result = [missing_number, [{", ".join([str(x) for x in sorted_duplicate])}]

# print(numbers_searching(1, 2, 4, 2, 5, 4))
#
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
