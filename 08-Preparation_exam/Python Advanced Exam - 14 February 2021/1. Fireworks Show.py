from collections import deque


def try_to_get_firework(current_effects, current_explosion):

    mix = current_explosion + current_effects
    if mix % 15 == 0:
        return "Crossette Fireworks"
    elif mix % 3 == 0:
        return "Palm Fireworks"
    elif mix % 5 == 0:
        return "Willow Fireworks"
    else:
        return None


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

firework_type = {
    'Willow Fireworks': 0,
    "Palm Fireworks": 0,
    'Crossette Fireworks': 0
}

is_successfull = False
while firework_effects and explosive_power:
    current_effects = firework_effects.popleft()
    if current_effects <= 0:
        continue
    current_explosion = explosive_power.pop()
    if current_explosion <= 0:
        firework_effects.appendleft(current_effects)
        continue
    result = try_to_get_firework(current_effects, current_explosion)
    if not result:
        current_effects -= 1
        firework_effects.append(current_effects)
        explosive_power.append(current_explosion)
        continue
    firework_type[result] += 1
    score = 0
    for value in firework_type.values():
        if value < 3:
            continue
        score += 1
    if score == 3:
        is_successfull = True
        break

if is_successfull:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in firework_effects])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosive_power])}')
sorted_firework_type = sorted(firework_type.items(), key=lambda x: len(x[0]))
for type_firework, value in sorted_firework_type:
    print(f'{type_firework}: {value}')
