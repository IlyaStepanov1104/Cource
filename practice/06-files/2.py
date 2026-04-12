# Создать программу, которая сохраняет имя, уровень и инвентарь персонажа в JSON файл. 
# При запуске загружает данные, позволяет изменить уровень и сохраняет обратно. 
# Обработать ошибки: 
#   файл не найден -> создать нового персонажа по умолчанию, 
#   испорченный JSON -> вывести ошибку.
import json

DEFAULT_PERSON = {"name": "Alex", "level": 95, "inventory": ['weapon']}

try:
    with open('person.json') as file:
        data = json.load(file)
except FileNotFoundError:
    data = DEFAULT_PERSON
except json.JSONDecodeError:
    print("Ошибка: некорректный JSON файл!")
    data = DEFAULT_PERSON

print(f"Имя: {data['name']}, Уровень: {data['level']}, Инвентарь: {data['inventory']}")

try:
    new_level = int(input('Введите новый уровень: '))
except ValueError:
    print("Ошибка: уровень должен быть числом!")
    new_level = DEFAULT_PERSON['level']
    
data["level"] = new_level

with open("person.json", "w") as file:
    json.dump(data, file)