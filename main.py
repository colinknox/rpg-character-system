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



yusuke = Character("Yusuke", 10_000)

print(f"Before health: {yusuke.health}")
yusuke.take_damage(9_999)
print(f"After health: {yusuke.health}")