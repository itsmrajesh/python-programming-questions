import random as r

class Dice:
    def roll(self):
        return (r.randint(1,6),r.randint(1,6))



d= Dice()
print(d.roll())

