rivers = {"nile": "egipt", "ebro": "spain", "rin": "germany"}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())
