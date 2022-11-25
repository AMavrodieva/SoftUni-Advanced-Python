from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
value_present = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents = {}
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic_level.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue
    total_magic = current_magic * current_material
    if total_magic in value_present:
        get_present = value_present[total_magic]
        if get_present not in presents:
            presents[get_present] = 0
        presents[get_present] += 1
        continue
    if total_magic < 0:
        materials.append(current_material + current_magic)
    else:
        materials.append(current_material + 15)


if ("Teddy bear" in presents and "Bicycle" in presents) or ("Doll" in presents and "Train" in presents):
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')
if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
for toy, value in sorted(presents.items()):
    print(f'{toy}: {value}')
