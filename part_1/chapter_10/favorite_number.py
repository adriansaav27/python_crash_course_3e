from pathlib import Path
import json

path = Path("./chapter_10/favorite_number.json")

number = input("Insert yout favorite number: ")

contents = json.dumps(number)
path.write_text(contents)
