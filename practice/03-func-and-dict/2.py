# Пользователь вводит имя и счёт. Когда вводит 0 - выводим всех
# Артём 65
# Иван 92
# Маша 78
# Артём 85
# Артём 45
# 0

d = {}

k = input("Введите счет: ")

while k != '0':
    name, score = k.split()
    score = int(score)
    
    if score > d.get(name, 0):
        d[name] = score
        
    k = input("Введите счет: ")
    
for key, value in d.items():
    print(f'{key}: {value}')