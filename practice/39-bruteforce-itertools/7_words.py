from itertools import product, permutations, combinations

# Верни слова длины length из ABC: ровно одна A, соседние буквы различны. length >= 1. Порядок лексикографический.
def valid_words(length: int) -> list[str]:
    res = []
    for chars in product('ABC', repeat=length):
        word = ''.join(chars)

        if word.count('A') == 1 and all(word[i] != word[i+1] for i in range(length - 1)):
            res.append(word)

        # if word.count('A') != 1:
        #     continue

        # for i in range(length - 1):
        #     if word[i] == word[i + 1]:
        #         break
        # else:
        #     res.append(word)

    return res




print(valid_words(2), ['AB', 'AC', 'BA', 'CA'])
print(valid_words(3), ['ABC', 'ACB', 'BAB', 'BAC', 'BCA', 'CAB', 'CAC', 'CBA'])
print(valid_words(1), ['A'])
