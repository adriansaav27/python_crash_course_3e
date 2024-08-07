from pathlib import Path

path = Path("./chapter_10/guest.txt")
text = ""

while True:
    user_name = input("Insert your name (introduce quit for exit): ")

    if user_name == "quit":
        break

    text += f"{user_name}\n"

path.write_text(text.strip())
