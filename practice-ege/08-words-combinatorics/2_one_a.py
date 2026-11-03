from itertools import product

# Слова длины 4 из АБВ; ровно одна А. Буквы могут повторяться.
def count_words() -> int:
    count = 0
    for chars in product('ШКОЛА', repeat=3):
        word = ''.join(chars)
        if word.count('К') == 1:
            count += 1
    return count




print(count_words(), 32)
