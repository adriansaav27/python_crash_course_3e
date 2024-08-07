from pathlib import Path

print("CATS")
try:
    path_cats = Path("./chapter_10/cats.txt")
    cats_contents = path_cats.read_text()
    for line in cats_contents.splitlines():
        print(f"\t{line}")
except:
    pass

print("DOGS")
try:
    path_dogs = Path("./chapter_10/dogs.txt")
    dogs_contents = path_dogs.read_text()
    for line in dogs_contents.splitlines():
        print(f"\t{line}")
except:
    pass
