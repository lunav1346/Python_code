class knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = knight(health=542.4, mana=201.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()