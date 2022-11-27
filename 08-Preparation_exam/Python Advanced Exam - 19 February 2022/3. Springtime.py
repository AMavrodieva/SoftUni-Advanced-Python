def start_spring(**kwargs):
    string = ''
    spring = {}
    for spring_object, object_type in kwargs.items():
        if object_type not in spring:
            spring[object_type] = []
        spring[object_type].append(spring_object)

    result = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple_object in result:
        type_object = tuple_object[0]
        list_object = tuple_object[1]
        sorted_list = sorted(list_object)
        string += f'{type_object}:\n'
        for type_o in sorted_list:
            string += f'-{type_o}\n'

    return string.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
