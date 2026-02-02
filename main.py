class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health



yusuke = Character("Yusuke", 10_000)

print(yusuke.name)
print(yusuke.health)