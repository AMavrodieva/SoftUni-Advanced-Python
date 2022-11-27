def stock_availability(list_of_boxes, action,  *args):
    boxes = list_of_boxes
    if action == "delivery":
        for arg in args:
            boxes.append(arg)
        return boxes
    elif action == 'sell':
        if not args:
            boxes.pop(0)
            return boxes
        else:
            for el in args:
                if str(el).isdigit():
                    for num in range(el):
                        if list_of_boxes:
                            boxes.pop(0)
                else:
                    if el in boxes:
                        boxes = [value for value in boxes if value != el]
            return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3, 'banana'))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
