from abc import ABC, abstractmethod
from typing import List

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp
        
    @abstractmethod
    def attack(self, target: Character):
        pass
    
    @property
    def hp(self):
        return self._hp
        
    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            return
        
        self._hp = value
        
        
    def is_alive(self) -> bool:
        return self._hp > 0
    
class Warrior(Character):
    damage = 20
    style = "Ближний бой"
    
    def attack(self, target):
        if target.is_alive():
            target.hp-=self.damage
            print(f"{self.name} атаковал {target.name} и нанес {self.damage} урона. У {target.name} осталось {target.hp} ХП")
        else: print(f"{target.name} уже мертв")
               
class Mage(Character):
    damage = 30
    style = "Заклинания"
    
    def attack(self, target):
        if target.is_alive():
            target.hp-=self.damage
            print(f"{self.name} атаковал {target.name} и нанес {self.damage} урона. У {target.name} осталось {target.hp} ХП")
        else: print(f"{target.name} уже мертв")

class Archer(Character):
    damage = 15
    style = "Дальний бой"
    
    def attack(self, target):
        if target.is_alive():
            target.hp-=self.damage
            print(f"{self.name} атаковал {target.name} и нанес {self.damage} урона. У {target.name} осталось {target.hp} ХП")
        else: print(f"{target.name} уже мертв")
    
class Team:
    def __init__(self, heroes: List[Character]):
        self.heroes = heroes
    
    def attack_enemy(self, enemy: Character):
        for hero in self.heroes:
            if enemy.is_alive():
                hero.attack(enemy)
            else:
                (f"{hero.name} погиб")
            
        
hero = Warrior('Hero', 100)

print('БИТВА НАЧИНАЕТСЯ!')
print()


team = Team([
    Warrior('Warior', 100), 
    Mage('Mage', 50), 
    Archer('Archer', 80)
])

goblin = Warrior('Goblin', 500)
while goblin.is_alive():
    team.attack_enemy(goblin)
print(f"{goblin.name} мертв")
