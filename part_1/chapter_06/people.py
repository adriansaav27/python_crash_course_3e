person1 = {
    "first_name" : "Adrián",
    "last_name" : "Saavedra",
    "age" : "25",
    "city" : "Barcelona",
}

person2 = {
    "first_name" : "Andra",
    "last_name" : "Cebuc",
    "age" : "23",
    "city" : "Logroño",
}

person3 = {
    "first_name" : "Andrew",
    "last_name" : "Martinez",
    "age" : "25",
    "city" : "Logroño",
}

people = [ person1, person2, person3 ]

for person in people:
    print(f"first_name -> {person["first_name"]}")
    print(f"last_name -> {person["last_name"]}")
    print(f"age -> {person["age"]}")
    print(f"city -> {person["city"]}")
