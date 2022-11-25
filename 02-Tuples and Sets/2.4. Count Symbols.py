text = input()
result = {}
for ch in text:
    if ch not in result:
        result[ch] = 0
    result[ch] += 1
for character, counts in sorted(result.items()):
    print(f'{character}: {counts} time/s')
