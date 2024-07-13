pet1 = {
    "kind" : "cat",
    "owner" : "Adrián"
}

pet2 = {
    "kind" : "dog",
    "owner" : "Andra"
}

pets = [ pet1, pet2 ]

for pet in pets:
    print(f"kind -> {pet["kind"]}")
    print(f"owner -> {pet["owner"]}")