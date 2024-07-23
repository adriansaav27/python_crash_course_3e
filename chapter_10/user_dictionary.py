from pathlib import Path
import json


def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def greet_user():
    path = Path("./chapter_10/user.json")
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user["username"]}!")
    else:
        user = get_new_user(path)
        for key, value in user.items():
            print(f"{key} -> {value}")


def get_new_user(path):
    data = {}

    username = input("What is your name? ")
    data["username"] = username

    age = input("What is your age? ")
    data["age"] = age

    favorite_color = input("What is your favorite color? ")
    data["favorite_color"] = favorite_color

    contents = json.dumps(data)
    path.write_text(contents)
    
    return data


greet_user()
