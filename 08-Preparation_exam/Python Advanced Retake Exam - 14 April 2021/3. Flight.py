def flights(*args):
    flight_to = {}
    for el in range(0, len(args), 2):
        if args[el] == "Finish":
            break
        flight = args[el]
        if flight not in flight_to:
            flight_to[flight] = 0
        flight_to[flight] += args[el+1]
    return flight_to


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
