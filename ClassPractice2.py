class Annie:
    def __init__(self, health, mana, Ability_power):
        self.health = health
        self.mana = mana
        self.Ability_power = Ability_power

    def tibbers(self):
        print('티버: 피해량 {0}'.format(self.Ability_power * 0.65 + 400))

health, mana, Ability_power = map(float, input().split())
x = Annie(health=health, mana=mana, Ability_power=Ability_power)
x.tibbers()