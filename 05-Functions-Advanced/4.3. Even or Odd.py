# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         even = []
#         for num in args[0:-1]:
#             if num % 2  == 0:
#                 even.append(num)
#         return even
#
#     else:
#         odd = []
#         for num in args[0:-1]:
#             if num % 2 == 1:
#                 odd.append(num)
#         return odd

# По-добър вариант
def even_odd(*args):
    command = args[-1]
    result = []
    parity = 0 if command == "even" else 1
    for num in args[0:-1]:
        if num % 2 == parity:
            result.append(num)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))