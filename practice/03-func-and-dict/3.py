# Пользователь вводит строку - посчитать, сколько раз встречается каждое слово

# кот пёс кот рыба кот пёс

words = input().split()
d = {}

for word in words:
    d[word] = d.get(word, 0) + 1
    
for key, value in d.items():
    print(f'{key}: {value}')