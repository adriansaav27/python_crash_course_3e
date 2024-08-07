from pathlib import Path

path = Path("./chapter_10/learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace("Python", "C"))
