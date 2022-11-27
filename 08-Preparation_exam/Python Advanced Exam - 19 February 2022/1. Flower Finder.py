from collections import deque


def create_dictionary(words):
    result = {}
    for el in words:
        if el not in result:
            result[el] = {}
        result[el] = {letter: False for letter in el}
    return result


def mark_words_letters(current_vowel, current_consonant, word, searched_word):
    result = False
    if current_vowel in word:
        searched_word[word][current_vowel] = True
        result = True
    if current_consonant in word:
        searched_word[word][current_consonant] = True
        result = True
    return result


vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]
words = ["rose", "tulip", "lotus", "daffodil"]
searched_word = create_dictionary(words)


matched_words = {}
found_word = ''
is_found = False
while vowels and consonants and not is_found:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for word in words:
        if mark_words_letters(current_vowel, current_consonant, word, searched_word):
            if all(searched_word[word].values()):
                found_word = word
                is_found = True
                break


if len(found_word) > 1:
    print(f'Word found: {found_word}')
else:
    print(f'Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join([str(x) for x in vowels])}')
if consonants:
    print(f'Consonants left: {" ".join([str(x) for x in consonants])}')
