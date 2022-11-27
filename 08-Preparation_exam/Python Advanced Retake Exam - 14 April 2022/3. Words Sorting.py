def words_sorting(*args):
    def calculate(word):
        return sum(ord(char) for char in word)
    dictionary = {word: calculate(word) for word in args}
    total_sum = sum(dictionary.values())
    if total_sum % 2 == 0:
        result = sorted(dictionary.items())
    else:
        result = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return "\n".join(f'{key} - {value}' for key, value in result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
