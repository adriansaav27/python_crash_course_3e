from pathlib import Path

path = Path("./chapter_10/learning_python.txt")
contents = path.read_text()
print(f"{contents}\n")

for line in contents.splitlines():
    print(line)
