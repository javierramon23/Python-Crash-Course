from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

die_one = Die()
die_two = Die(10)
die_three = Die(20)

indice = 0
while indice < 10:
    die_three.roll_die()
    indice += 1