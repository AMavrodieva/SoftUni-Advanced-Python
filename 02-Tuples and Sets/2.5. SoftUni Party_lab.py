def is_vip(guest):
    return guest[0].isdigit()


number_of_guest = int(input())
vip_guest = set()
regular_guest = set()

for _ in range(number_of_guest):
    reservation_code = input()
    if is_vip(reservation_code):
        vip_guest.add(reservation_code)
    else:
        regular_guest.add(reservation_code)

while True:
    command = input()
    if command == "END":
        break
    if is_vip(command):
        vip_guest.remove(command)
    else:
        regular_guest.remove(command)
print(len(vip_guest)+len(regular_guest))

[print(guest)for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(regular_guest)]

# Вариант 2

def is_vip(guest):
    return guest[0].isdigit()


number_of_guest = int(input())
vip_guest = set()
regular_guest = set()

for _ in range(number_of_guest):
    reservation_code = input()
    if is_vip(reservation_code):
        vip_guest.add(reservation_code)
    else:
        regular_guest.add(reservation_code)
command = input()
while command != "END":
    if command in vip_guest:
        vip_guest.remove(command)
    elif command in regular_guest:
        regular_guest.remove(command)
    command = input()
print(len(vip_guest)+len(regular_guest))
# print(*(sorted(vip_guest)), sep='\n')
# print(*(sorted(regular_guest)), sep='\n')
[print(guest)for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(regular_guest)]