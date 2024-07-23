from pathlib import Path
import json

path = Path("./chapter_10/favorite_number.json")

contents = path.read_text()
favorite_number = json.loads(contents)

print(f"I know your favorite number! It’s {favorite_number}")
