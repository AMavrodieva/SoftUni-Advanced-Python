# import unittest


def grocery_store(**kwargs):
    sorted_store = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    store_result = [f'{key}: {value}' for key, value in sorted_store]
    return "\n".join(store_result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


# class Tests(unittest.TestCase):
#     def test(self):
#         res = grocery_store(bread=5,
#                             pasta=12,
#                             eggs=12,
#                             )
#         self.assertEqual(res.strip(),
#                          "pasta: 12\n"
#                          "eggs: 12\n"
#                          "bread: 5")
#
#
# if __name__ == "__main__":
#     unittest.main()