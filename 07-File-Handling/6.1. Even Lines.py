from os.path import sep

symbols = ["-", ",", ".", "!", "?"]

with open('./text.txt', 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for sym in symbols:
                result = result.replace(sym, "@")
            print(result)

