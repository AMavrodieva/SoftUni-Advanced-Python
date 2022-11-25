box_of_clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())
current_capacity = capacity_of_rack
count_of_racks = 1
while box_of_clothes:
    current_box = box_of_clothes[-1]
    if current_box <= current_capacity:
        box_of_clothes.pop()
        current_capacity -= current_box
    else:
        count_of_racks += 1
        current_capacity = capacity_of_rack
print(count_of_racks)