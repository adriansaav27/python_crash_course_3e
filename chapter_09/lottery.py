from random import randint

enumeration = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

print("Any ticket matching these 4 numbers or letters wins a prize!")

for item in range(1, 4 + 1):
    position = randint(0, len(enumeration) - 1)
    ticket = enumeration.pop(position)
    print(f"\t>>> {ticket}")
