def shopping_cart(*args):
    result = ""
    list_of_product = [x for x in args]
    limit_of_product = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    shopping_list = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    for el in list_of_product:
        if el == "Stop":
            break
        type_of_meal = el[0]
        product_for_meal = el[1]
        if product_for_meal in shopping_list[type_of_meal]:
            continue
        if len(shopping_list[type_of_meal]) >= limit_of_product[type_of_meal]:
            continue
        shopping_list[type_of_meal].append(product_for_meal)

    sorted_list = sorted(shopping_list.items(), key=lambda x: (-len(x[1]), x[0]))

    number = 0
    for key, value in sorted_list:
        if len(value) >= 1:
            number += 1
    if number < 1:
        return "No products in the cart!"
    for key, value in sorted_list:
        result += f'{key}:\n'
        for el in sorted(value):
            result += f'- {el}\n'
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
