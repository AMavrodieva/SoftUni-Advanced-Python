from collections import deque

elf_energy = deque([int(x) for x in input().split(" ")])
materials = [int(x) for x in input().split()]

total_energy = 0
toys = 0
count_attempt = 0

while elf_energy and materials:
    while elf_energy and elf_energy[0] < 5:
        elf_energy.popleft()
    if not elf_energy:
        break

    current_elf = elf_energy.popleft()
    current_box = materials.pop()
    count_attempt += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = current_box
    energy_increase_factory = 1

    if count_attempt % 3 == 0:
        energy_to_be_spent *= 2
        toys_to_be_created_count = 2
    if count_attempt % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= current_elf:
        toys += toys_to_be_created_count
        total_energy += energy_to_be_spent
        elf_energy.append(current_elf - energy_to_be_spent + energy_increase_factory)
    else:
        materials.append(current_box)
        elf_energy.append(current_elf * 2)

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if elf_energy:
    print(f'Elves left: {", ".join([str(x) for x in elf_energy])}')
if materials:
    print(f'Boxes left: {", ".join([str(y) for y in materials])}')
