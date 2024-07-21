from random import randint

enumeration = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
my_ticket = [1]

while True:
    position = randint(0, len(enumeration) - 1)
    ticket = enumeration.pop(position)
    print(f"\t>>> {ticket}")

    if my_ticket[0] == ticket:
        print(f"\t>>> You WINS!")
        break
