# Результат урока 14

## Структура файлов

```
python-rpg/
├── config.py       # без изменений
├── characters.py   # + Equipment, Boss, weapon/armor слоты, equip()
├── item.py         # без изменений
├── items.py        # + WOODEN_SWORD, CHAINMAIL, STEEL_SWORD, SHIELD
├── inventory.py    # без изменений
├── logger.py       # без изменений
├── fight.py        # + награда зависит от уровня врага
├── tavern.py       # + раздел снаряжения
├── save.py         # + сохранение/загрузка weapon и armor
└── main.py         # + выбор героя, ARENA, scale_enemy
```

---

## characters.py

```python
from abc import ABC, abstractmethod
from random import randint
from inventory import Inventory
from logger import logger


class Character(ABC):
    _hp = 100
    max_hp = 150
    damage = 20

    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self._gold = 0
        self.level = 1
        self.xp = 0
        self.xp_threshold = 100
        self.weapon = None
        self.armor = None

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(self.max_hp, value))

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = max(0, value)

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_threshold:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.damage += 5
        self.xp_threshold = int(self.xp_threshold * 1.5)
        logger.log_level_up(self)

    def equip(self, item):
        if item.bonus_damage:
            self.weapon = item
        if item.bonus_armor:
            self.armor = item

    def to_dict(self):
        return {
            "class":         self.__class__.__name__,
            "name":          self.name,
            "level":         self.level,
            "xp":            self.xp,
            "xp_threshold":  self.xp_threshold,
            "gold":          self.gold,
            "damage":        self.damage,
            "hp":            self.hp,
            "max_hp":        self.max_hp,
            "inventory":     [item.name for item in self.inventory.items],
            "weapon":        self.weapon.name if self.weapon else None,
            "armor":         self.armor.name  if self.armor  else None,
        }

    @classmethod
    def from_dict(cls, data):
        hero = cls(data["name"])
        hero.level        = data["level"]
        hero.xp           = data["xp"]
        hero.xp_threshold = data["xp_threshold"]
        hero.gold         = data["gold"]
        hero.damage       = data["damage"]
        hero.max_hp       = data["max_hp"]
        hero.hp           = data["hp"]
        return hero

    def __str__(self):
        return f"'{self.name}' [HP {self._hp}/{self.max_hp}]"

    @abstractmethod
    def attack(self, target):
        pass


class Warior(Character):
    _hp = 145
    max_hp = 170
    damage = 20
    armour = 5

    def take_damage(self, amount):
        armor_bonus = self.armor.bonus_armor if self.armor else 0
        real = max(0, amount - self.armour - armor_bonus)
        super().take_damage(real)

    def attack(self, target):
        bonus = self.weapon.bonus_damage if self.weapon else 0
        total = self.damage + bonus
        target.take_damage(total)
        return total


class Mage(Character):
    _hp = 70
    max_hp = 120
    damage = 30
    counter_attack = 0

    def attack(self, target):
        self.counter_attack += 1
        bonus = self.weapon.bonus_damage if self.weapon else 0
        amount = (self.damage + bonus) * 3 if self.counter_attack % 3 == 0 else self.damage + bonus
        target.take_damage(amount)
        return amount


class Archer(Character):
    _hp = 90
    max_hp = 140
    damage = 15

    def attack(self, target):
        bonus = self.weapon.bonus_damage if self.weapon else 0
        total = self.damage + bonus
        target.take_damage(total)
        if randint(0, 1):
            target.take_damage(total)
            return total * 2
        return total


class Boss(Character):
    _hp = 300
    max_hp = 300
    damage = 45

    def __init__(self, name):
        super().__init__(name)
        self.counter = 0

    def attack(self, target):
        self.counter += 1
        if self.counter % 3 == 0:
            healed = min(40, self.max_hp - self._hp)
            self._hp += healed
            print(f"{self.name} восстанавливает {healed} HP!")
            return 0
        target.take_damage(self.damage)
        return self.damage
```

---

## item.py

```python
class Item:
    def __init__(self, name, style, value=0):
        self.name = name
        self.style = style
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.style} {self.value})"


class Equipment(Item):
    def __init__(self, name, bonus_damage=0, bonus_armor=0):
        super().__init__(name, style="equip")
        self.bonus_damage = bonus_damage
        self.bonus_armor  = bonus_armor

    def __str__(self):
        parts = []
        if self.bonus_damage:
            parts.append(f"+{self.bonus_damage} урон")
        if self.bonus_armor:
            parts.append(f"+{self.bonus_armor} броня")
        return f"{self.name} ({', '.join(parts)})"
```

---

## items.py

```python
from item import Item, Equipment

HEALTH_POTION     = Item("Зелье здоровья",       "heal",   30)
BIG_HEALTH_POTION = Item("Большое зелье здоровья","heal",   60)
POISON_POTION     = Item("Зелье урона",           "damage", 30)
BIG_POISON_POTION = Item("Большое зелье урона",   "damage", 60)

WOODEN_SWORD = Equipment("Деревянный меч", bonus_damage=5)
CHAINMAIL    = Equipment("Кольчуга",       bonus_armor=3)
STEEL_SWORD  = Equipment("Стальной меч",   bonus_damage=10)
SHIELD       = Equipment("Щит",            bonus_armor=5)
```

---

## tavern.py

```python
from characters import Character
from items import (HEALTH_POTION, BIG_HEALTH_POTION,
                   POISON_POTION, BIG_POISON_POTION,
                   WOODEN_SWORD, CHAINMAIL, STEEL_SWORD, SHIELD)

SHOP = [
    (HEALTH_POTION,     30),
    (BIG_HEALTH_POTION, 60),
    (POISON_POTION,     25),
    (BIG_POISON_POTION, 50),
]

SHOP_EQUIPMENT = [
    (WOODEN_SWORD, 40),
    (CHAINMAIL,    50),
    (STEEL_SWORD,  80),
    (SHIELD,       70),
]


def _show_and_buy(hero, shop, equip=False):
    while True:
        print()
        for i, (item, price) in enumerate(shop):
            print(f"[{i}] {item.name} - {price}g")
        print("[q] Назад")

        choice = input("Выбор: ").strip()
        if choice == "q":
            break
        if not choice.isdigit() or int(choice) >= len(shop):
            print("Неверный выбор")
            continue

        item, price = shop[int(choice)]
        if hero.gold < price:
            print(f"Не хватает gold. Нужно {price}, есть {hero.gold}")
            continue

        hero.gold -= price
        if equip:
            hero.equip(item)
            print(f"Надето: {item}. Осталось gold: {hero.gold}")
        else:
            hero.inventory.add_item(item)
            print(f"Куплено: {item.name}. Осталось gold: {hero.gold}")


def tavern(hero: Character):
    while True:
        weapon_str = str(hero.weapon) if hero.weapon else "нет"
        armor_str  = str(hero.armor)  if hero.armor  else "нет"
        print(f"\n=== ТАВЕРНА === | Gold: {hero.gold}")
        print(f"Оружие: {weapon_str} | Броня: {armor_str}")
        print()
        print("[1] Зелья")
        print("[2] Снаряжение")
        print("[q] Выйти")

        choice = input("Выбор: ").strip()
        if choice == "q":
            break
        elif choice == "1":
            _show_and_buy(hero, SHOP, equip=False)
        elif choice == "2":
            _show_and_buy(hero, SHOP_EQUIPMENT, equip=True)
```

---

## save.py

```python
import json
from characters import Warior, Mage, Archer
from items import (HEALTH_POTION, BIG_HEALTH_POTION,
                   POISON_POTION, BIG_POISON_POTION,
                   WOODEN_SWORD, CHAINMAIL, STEEL_SWORD, SHIELD)
from config import SAVE_PATH

CLASSES = {
    "Warior": Warior,
    "Mage":   Mage,
    "Archer": Archer,
}

ITEMS = {
    HEALTH_POTION.name:     HEALTH_POTION,
    BIG_HEALTH_POTION.name: BIG_HEALTH_POTION,
    POISON_POTION.name:     POISON_POTION,
    BIG_POISON_POTION.name: BIG_POISON_POTION,
}

EQUIPMENT = {
    WOODEN_SWORD.name: WOODEN_SWORD,
    CHAINMAIL.name:    CHAINMAIL,
    STEEL_SWORD.name:  STEEL_SWORD,
    SHIELD.name:       SHIELD,
}


def save_hero(hero, path=SAVE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(hero.to_dict(), f, ensure_ascii=False, indent=2)


def load_hero(path=SAVE_PATH):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    cls = CLASSES[data["class"]]
    hero = cls.from_dict(data)
    for name in data.get("inventory", []):
        if name in ITEMS:
            hero.inventory.add_item(ITEMS[name])
    if data.get("weapon") and data["weapon"] in EQUIPMENT:
        hero.equip(EQUIPMENT[data["weapon"]])
    if data.get("armor") and data["armor"] in EQUIPMENT:
        hero.equip(EQUIPMENT[data["armor"]])
    return hero
```

---

## fight.py

```python
from random import random, choice
from characters import Character
from config import DROPS, FIGHT_LIMIT
from logger import logger

GOLD_BASE = 30
XP_BASE   = 40


def generate_drop():
    if random() < 0.7:
        return choice(DROPS)
    return None


def player_turn(hero, enemy):
    print(f"\n=== Твой ход ===")
    print(f"{hero.name}: HP {hero.hp}/{hero.max_hp} | Gold: {hero.gold} | Инвентарь: {hero.inventory}")
    print(f"{enemy.name}: HP {enemy.hp}/{enemy.max_hp}")
    print()
    print("[1] Атаковать")
    if hero.inventory.items:
        print("[2] Использовать предмет")
    print("[3] Выход из боя")

    choice_input = input("Выбор: ").strip()

    if choice_input == "3":
        return True

    if choice_input == "2" and hero.inventory.items:
        for i, item in enumerate(hero.inventory.items):
            print(f"  [{i}] {item}")
        idx = int(input("Какой предмет: "))
        item = hero.inventory.items[idx]
        if item.style == "heal":
            hero.inventory.use_item(idx, hero)
            logger.log_use_heal_item(hero, item)
        elif item.style == "damage":
            hero.inventory.use_item(idx, enemy)
            logger.log_use_damage_item(hero, enemy, item)
    else:
        damage = hero.attack(enemy)
        logger.log_attack(hero, enemy, damage)

    return False


def fight(player: Character, enemy: Character):
    print(f"\n=== БОЙ ===")
    print(f"{player} vs {enemy}\n")

    for _ in range(FIGHT_LIMIT):
        fled = player_turn(player, enemy)

        if fled:
            logger.log_exit(player)
            return None

        if not enemy.is_alive():
            logger.log_winner(player)
            player.gold += GOLD_BASE * enemy.level
            player.gain_xp(XP_BASE * enemy.level)
            drop = generate_drop()
            if drop:
                player.inventory.add_item(drop)
                logger.log_drop(drop)
            return player

        damage = enemy.attack(player)
        if damage > 0:
            logger.log_attack(enemy, player, damage)
        if not player.is_alive():
            logger.log_winner(enemy)
            return enemy

    return None
```

---

## main.py

```python
import os
from characters import Archer, Mage, Warior, Boss
from config import SAVE_PATH
from fight import fight
from items import HEALTH_POTION, POISON_POTION
from logger import logger
from tavern import tavern
from save import save_hero, load_hero

CLASSES = {
    "1": Warior,
    "2": Mage,
    "3": Archer,
}

ARENA = [
    (Archer, "Скай",   1),
    (Mage,   "Торин",  2),
    (Warior, "Кратос", 3),
    (Boss,   "Игниус", 5),
]


def scale_enemy(cls, name, level):
    enemy = cls(name)
    for _ in range(level - 1):
        enemy.level_up()
    return enemy


def get_hero():
    if os.path.exists(SAVE_PATH):
        choice = input("Найдено сохранение. Загрузить? (y/n): ").strip()
        if choice == "y":
            return load_hero(SAVE_PATH)

    name = input("Имя героя: ").strip() or "Герой"
    print("[1] Воин  [2] Маг  [3] Лучник")
    cls = CLASSES.get(input("Класс: ").strip(), Warior)
    hero = cls(name)
    hero.inventory.add_item(HEALTH_POTION)
    hero.inventory.add_item(POISON_POTION)
    return hero


hero = get_hero()

for i, (cls, name, level) in enumerate(ARENA):
    remaining = len(ARENA) - i
    print(f"\nВпереди противников: {remaining}")

    tavern(hero)
    enemy = scale_enemy(cls, name, level)
    result = fight(hero, enemy)

    if not hero.is_alive():
        logger.log_death(hero)
        break

    if result is None:
        print("Бой прерван")
        continue

    hero._hp = min(hero.max_hp, hero._hp + 30)
    print(f"Отдых: +30 HP. Сейчас: {hero.hp}/{hero.max_hp}")
    save_hero(hero)
else:
    print("\nАрена пройдена! Поздравляем!")
```
