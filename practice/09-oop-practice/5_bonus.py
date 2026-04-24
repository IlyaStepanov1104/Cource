# Бонус: Shape по SOLID
#
# У тебя уже есть Shape, Circle, Rectangle с прошлого занятия.
# Напиши функцию print_areas(shapes), которая принимает ЛЮБОЙ
# список фигур и печатает их площади.
#
# Подумай:
# 1. Какой принцип SOLID это иллюстрирует?
#    (Подсказка: мы ничего не меняем в функции, если добавляем новый тип фигуры)
# 2. Что нужно будет сделать, чтобы добавить класс Hexagon?

from abc import ABC, abstractmethod
from math import pi, ceil


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return ceil(pi * self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Напиши функцию:
def print_areas(shapes):
    pass


# Проверка
# shapes = [Circle(5), Rectangle(4, 6)]
# print_areas(shapes)
#
# Добавь новый Hexagon и убедись, что print_areas не нужно менять
