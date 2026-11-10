from itertools import permutations

# ДЗ прошлого урока: пятизначные восьмеричные числа без 1.
# Все цифры различны, чётности соседних цифр чередуются.
c = 0
for ch in permutations('0234567', r = 5):
    word = ''.join(ch)
    if word[0] == '0':
        continue
    for i in range(len(word)-1):
        if (word[i] in '0246' and word[i+1] in '0246') or (word[i] in '357' and word[i+1] in '357'):
            break
    else:
        c += 1
print(c)