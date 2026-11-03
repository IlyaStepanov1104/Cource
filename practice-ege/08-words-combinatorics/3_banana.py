from itertools import permutations

def count_words() -> int:
    s = []
    for chars in permutations('СВЕТЛАНА', 8):
        word = ''.join(chars)
        if 'АА' not in word:
            s.append(word)
    return len(set(s))




print(count_words())
