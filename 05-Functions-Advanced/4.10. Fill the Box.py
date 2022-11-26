def fill_the_box(height, length, width, *args):
    list_of_items = [*args]
    volume_box = height * length * width
    index = 0
    for el in list_of_items:
        if el == "Finish":
            return f'There is free space in the box. You could put {volume_box} more cubes.'
        if el <= volume_box:
            volume_box -= el
            index += 1
        else:
            cur_el = el - volume_box
            current_index = list_of_items.index(el)
            command_index = list_of_items.index("Finish")
            list_of_items[current_index] = cur_el
            left_items_sum = sum([list_of_items[x] for x in range(index, command_index)])
            return f'No more free space! You have {left_items_sum} more cubes.'


# Второ решение от лекцията
# def fill_the_box(height, length, width, *args):
#     volume_box = height * length * width
#     left_cubed = 0
#     for el in args:
#         if el == "Finish":
#             break
#         if el <= volume_box:
#             volume_box -= el
#         else:
#             el -= volume_box
#             left_cubed += el
#             volume_box = 0
#     if volume_box:
#         return f'There is free space in the box. You could put {volume_box} more cubes.'
#     else:
#         return f'No more free space! You have {left_cubed} more cubes.'

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
