from collections import deque


def check_for_bomb(current_effect, current_casing):
    mix = current_effect + current_casing
    if mix in bombs:
        result = bombs[mix]
        collected_bombs[result] += 1
        return True


bombs = {
        40: "Datura Bombs",
        60: "Cherry Bombs",
        120: "Smoke Decoy Bombs"
    }

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casing = [int(x) for x in input().split(", ")]

collected_bombs = {value: 0 for key, value in bombs.items()}

is_collected = False

while bomb_effect and bomb_casing and not is_collected:
    collected = 0
    current_effect = bomb_effect.popleft()
    if current_effect < 0:
        continue
    current_casing = bomb_casing.pop()
    if current_casing < 0:
        bomb_effect.appendleft(current_effect)
        continue
    if not check_for_bomb(current_effect, current_casing):
        current_casing -= 5
        bomb_casing.append(current_casing)
        bomb_effect.appendleft(current_effect)
        continue
    for key, value in collected_bombs.items():
        if value >= 3:
            collected += 1

        if collected == 3:
            is_collected = True

if is_collected:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effect)}')
else:
    print(f'Bomb Effects: empty')
if bomb_casing:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casing])}')
else:
    print(f'Bomb Casings: empty')
sorted_bombs = sorted(collected_bombs.items())
[print(f'{key}: {value}') for key, value in sorted_bombs]


