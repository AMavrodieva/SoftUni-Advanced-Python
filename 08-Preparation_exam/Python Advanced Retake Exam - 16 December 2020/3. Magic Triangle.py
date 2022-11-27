def get_magic_triangle(n):
    boxes = [[1], [1, 1]]
    el = boxes[0]
    for x in range(2,n+1):
        new_el = el * (x+1)
        boxes.append(new_el)
        for ind, y in enumerate(boxes):
            if ind in range(1, x):
                y = sum(boxes[x-1])

    return boxes

print(get_magic_triangle(5))
