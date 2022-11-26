text = input()

try:
    times = int(input())
    text = text * times
    print(text)

except ValueError:
    print(f'Variable times must be an integer')
