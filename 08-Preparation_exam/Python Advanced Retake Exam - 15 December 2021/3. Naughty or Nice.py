def naughty_or_nice_list(list_of_kids_name, *args, **kwargs):
    nice, naughty, not_found = [], [], []

    for arg in args:
        number, description = arg.split('-')
        number = int(number)
        is_unique = False
        name = None
        for counting_number, kid_name in list_of_kids_name:
            if number == counting_number and is_unique:
                is_unique = False
                break
            if number == counting_number:
                name = kid_name
                is_unique = True
        if is_unique:
            if description == "Nice":
                nice.append(name)
            elif description == "Naughty":
                naughty.append(name)
            list_of_kids_name.remove((number, name))

    for name_of_kids, characteristic in kwargs.items():
        is_unique = False
        number = None
        for counting_number, kid_name in list_of_kids_name:
            if name_of_kids == kid_name and is_unique:
                is_unique = False
                break
            if name_of_kids == kid_name:
                is_unique = True
                number = counting_number
        if is_unique:
            if characteristic == "Nice":
                nice.append(name_of_kids)
            elif characteristic == "Naughty":
                naughty.append(name_of_kids)
            list_of_kids_name.remove((number, name_of_kids))

    not_found = [kid_name for _, kid_name in list_of_kids_name]

    result = ''
    if nice:
        result += f'Nice: {", ".join(nice)}\n'
    if naughty:
        result += f'Naughty: {", ".join(naughty)}\n'
    if not_found:
        result += f'Not found: {", ".join(not_found)}\n'

    return result

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
