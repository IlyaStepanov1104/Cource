# Задача 2: Зоопарк
#
# Абстрактный Animal.feed(), наследники - свои реализации.
#
# Animal (ABC): метод feed()
# Lion, Rabbit, Parrot: каждый ест своё
# Zoo: список animals, метод feed_all()
#
# zoo = Zoo([Lion(), Rabbit(), Parrot()])
# zoo.feed_all()
# Лев ест мясо
# Кролик ест морковку
# Попугай ест зерно

from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def feed(self): pass
    
class Lion(Animal):
    def feed(self):
        print("Лев ест мясо")
    
class Rabbit(Animal):
    def feed(self):
        print("Кролик ест морковку")
    
class Parrot(Animal):
    def feed(self):
        print("Попугай ест зерно")

class Zoo:
    def __init__(self, animals: List[Animal]):
        self.animals = animals
        
    def feed_all(self):
        for animal in self.animals:
            animal.feed()

# Проверка
zoo = Zoo([Lion(), Rabbit(), Parrot()])
zoo.feed_all()
