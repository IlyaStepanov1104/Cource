# Задача: Класс Student
# Опиши класс Student с атрибутами name и grades (список оценок)
# и методом average(), который возвращает средний балл.


class Student:
    def __init__(self, name, grades):
        # TODO: сохрани атрибуты
        pass

    def average(self):
        # TODO: верни средний балл
        pass


s = Student("Аня", [5, 4, 5, 3])
print(s.name)        # Аня
print(s.average())   # 4.25
