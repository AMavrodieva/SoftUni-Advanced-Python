# number_of_cars = int(input())
# parking_lot = set()
# for _ in range(number_of_cars):
#     command, car_number = input().split(', ')
#     if command == "IN":
#         parking_lot.add(car_number)
#     elif command == "OUT" and parking_lot:
#         parking_lot.remove(car_number)
# if len(parking_lot) > 0:
#     print(*parking_lot, sep='\n')
# else:
#     print('Parking Lot is Empty')

number_of_cars = int(input())
parking_lot_log = [input().split(', ') for _ in range(number_of_cars)]
parking_lot = set()
for command, car_number in parking_lot_log:
    if command == "IN":
        parking_lot.add(car_number)
    elif command == "OUT" and parking_lot:
        parking_lot.remove(car_number)
if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print('Parking Lot is Empty')