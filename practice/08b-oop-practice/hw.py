# Создать абстрактный класс Character (наследник ABC) с атрибутами 
# name, 
# hp 
# и абстрактным методом attack(target). 
# 
# Реализовать наследников: 
# Warrior (ближний бой, урон 20), 
# Mage (заклинания, урон 30, но hp меньше), 
# Archer (дальний бой, урон 15). 
# 
# Добавить @property для hp с сеттером, который не даёт задать hp ниже 0. 
# Добавить метод is_alive().
 
# Создать класс Team со списком героев и методом 
# attack_enemy(enemy) - каждый живой член команды атакует врага. 
# Продемонстрировать бой команды против одного героя в цикле, пока враг не умрёт.

from abc import ABC, abstractmethod
from typing import List

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    @abstractmethod
    def attack(self, target: Character):
        pass
    
    @property
    def hp(self):
        ???
        
    @hp.setter
    def set_hp(self):
        ???
        
    def is_alive(self) -> bool:
        return self.hp > 0
    
class Warrior(Character):
    damage = 20
    style = "Ближний бой"
    
    def attack(target):
        ???
        
class Mage(Character):
    damage = 30
    style = "Заклинания"
    
    def attack(target):
        ???

class Archer(Character):
    damage = 15
    style = "Дальний бой"
    
    def attack(target):
        ???
    
class Team:
    def __init__(self, heroes: List[Character]):
        self.heroes = heroes
    
    def attack_enemy(self, enemy: Character):
        for hero in self.heroes:
            print('')
            hero.attack(enemy)
        
hero = Warrior('Hero', 100)
hero.hp = -10 -> Ошибка - нельзя hp < 0


team = Team([
    Warrior('Warior', 100), 
    Mage('Mage', 50), 
    Archer('Archer', 80)
])

goblin = Warrior('Goblin', 500)

team.attack_enemy(goblin)
team.attack_enemy(goblin)
team.attack_enemy(goblin)

# Пока goblin не умрет

team.attack_enemy(goblin)