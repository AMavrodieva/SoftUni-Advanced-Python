from _collections import deque


def is_made_present(current_material, current_magic, attempt):
    if attempt > 2:
        result = 0
        return result
    result = current_material + current_magic
    if result < 100:
        if result % 2 == 0:
            current_material *= 2
            current_magic *= 3
        else:
            current_material *= 2
            current_magic *= 2
    elif result > 499:
        current_material //= 2
        current_magic //= 2
    else:
        return result
    return is_made_present(current_material, current_magic, attempt+1)


def get_present(present, present_count):
    current_gift = ''
    for gift, amount in present.items():
        if present_count in range(amount[0], amount[1]+1):
            current_gift = gift
            break
    return current_gift


materials = [int(x) for x in input().split(" ")]
magic_levels = deque([int(x) for x in input().split(" ")])

present = {
    "Gemstone": [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499]
}


matched_gift = {}
while materials and magic_levels:
    attempt = 1
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    present_count = is_made_present(current_material, current_magic, attempt)
    if present_count != 0:
        current_present = get_present(present, present_count)
        if current_present not in matched_gift:
            matched_gift[current_present] = 0
        matched_gift[current_present] += 1

if ("Gemstone" in matched_gift and "Porcelain Sculpture" in matched_gift) \
    or ("Gold" in matched_gift and "Diamond Jewellery" in matched_gift):
    print(f'The wedding presents are made!')
else:
    print(f'Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(x) for x in magic_levels])}')
for gift, value in sorted(matched_gift.items()):
    print(f'{gift}: {value}')
