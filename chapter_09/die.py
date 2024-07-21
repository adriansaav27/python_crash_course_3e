from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


die = Die()
for iterator in range(1, 10 + 1):
    print(f"Roll {iterator}: {die.roll_dice()}")
print("\n")

die = Die(10)
for iterator in range(1, 10 + 1):
    print(f"Roll {iterator}: {die.roll_dice()}")
print("\n")

die = Die(20)
for iterator in range(1, 10 + 1):
    print(f"Roll {iterator}: {die.roll_dice()}")
print("\n")
