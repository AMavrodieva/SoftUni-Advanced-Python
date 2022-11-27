def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = {}
    have_enough_money = True
    for type_of_products, tuple_of_sum in kwargs.items():
        if len(basket) <= 4 and have_enough_money:
            price, quantity = tuple_of_sum
            result = float(price) * int(quantity)
            if result == 0:
                have_enough_money = False
                break
            if budget >= result:
                budget -= result
                if type_of_products not in basket:
                    basket[type_of_products] = 0
                basket[type_of_products] += result
                kwargs[type_of_products] = (0, 0)
            else:
                kwargs[type_of_products] = (0, 0)

    result = ''
    for key, value in basket.items():
        result += f'You bought {key} for {value:.2f} leva.\n'
    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

