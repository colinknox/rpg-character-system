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


# yusuke = Character("Yusuke", 10_000)
# print(f"Before health: {yusuke.health}")
# yusuke.take_damage(9_999)
# print(f"After health: {yusuke.health}")

conan = Warrior("Conan", 100, 25)
# print(conan.name)
# print(conan.health)
# print(conan.strength)
# print(conan.attack())
print(conan.get_armor())
print(conan.repair_armor(5))
print(conan.get_armor())
