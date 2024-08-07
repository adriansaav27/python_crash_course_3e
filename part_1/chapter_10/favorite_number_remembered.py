from pathlib import Path
import json

path = Path("./chapter_10/favorite_number.json")

number = input("Insert yout favorite number: ")

contents = path.read_text()
favorite_number = json.loads(contents)

if number == favorite_number:
    print("The number is already inserted :(")
else:
    contents = json.dumps(number)
    path.write_text(contents)
