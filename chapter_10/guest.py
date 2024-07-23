from pathlib import Path

user_name = input("Insert your name: ")
path = Path("./chapter_10/guest.txt")
path.write_text(user_name)
