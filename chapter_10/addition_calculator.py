from pathlib import Path

path = Path("./chapter_10/guest.txt")
text = ""

while True:

    try:
        user_input = input("Insert a number (introduce quit for exit): ")
        if user_input == "quit":
            break
        user_input = int(user_input)
    except:
        print("Is not a number!")
    else:
        text += f"{user_input}\n"

path.write_text(text)
