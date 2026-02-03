class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_stats(self):
        return f"Name: {self.name}, Health: {self.health}"
    
    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.health = 0

class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength
        self.__armor = 10

    def attack(self):
        return self.strength * 2

    def get_armor(self):
        return self.__armor
    
    def repair_armor(self, amount):
        self.__armor += amount

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast_spell(self, mana_cost):
        if self.__mana >= mana_cost:
            self.__mana -= mana_cost
            return True
        else:
            return False
        
    def get_mana(self):
        return self.__mana

    def meditate(self):
        self.__mana += 20
