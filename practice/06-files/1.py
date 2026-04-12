age = int(input("Возраст: "))

def print_age(age):    
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным!")

    print(f"Тебе {age} лет")
    
    
try: 
    print_age(age)
except ValueError:
    print("Вы ввели некорректный возраст!") 