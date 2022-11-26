from string import punctuation
from os import sep


def count_symbols(line):
    letters = 0
    punctuations = 0
    symbols = set(punctuation)
    for symbol in line:
        if symbol in symbols:
            punctuations += 1
        elif symbol.isalpha():
            letters += 1
    return letters, punctuations


with open(f'.{sep}text.txt', 'r') as input_file, open(f'.{sep}output.txt', 'w') as output_file :
    for index, line in enumerate(input_file):
        letters, punctuations = count_symbols(line)
        output_file.write(f'Line {index+ 1}: {line.strip()} ({letters})({punctuations})\n')