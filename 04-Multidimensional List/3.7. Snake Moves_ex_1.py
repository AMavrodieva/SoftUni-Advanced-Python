rows, columns = [int(x) for x in input().split()]
word = input()

index = 0
for row in range(rows):
    symbol = [None] * columns
    if row % 2 == 0:
        for col in range(columns):
            symbol[col] = word[index % len(word)]
            index += 1
    else:
        for col in range(columns-1, -1, -1):
            symbol[col] = word[index % len(word)]
            index += 1
    print(*symbol, sep='')