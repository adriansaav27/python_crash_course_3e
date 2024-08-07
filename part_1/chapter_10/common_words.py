from pathlib import Path

words = 0
path = Path("./chapter_10/example_text.txt")
contents = path.read_text()

for line in contents.splitlines():
    words = line.lower().count("the ")

print(f"Number of 'the': {words}")
