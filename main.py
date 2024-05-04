
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец выбирает лук")

    def fight(self):
        print(self.weapon.attack())
        print("Монстр побежден")

class Monster():
    def __init__(self):
        pass

sword1 = Sword()
bow1 = Bow()
fighter = Fighter(sword1)
fighter.fight()
fighter.change_weapon(bow1)
fighter.fight()




