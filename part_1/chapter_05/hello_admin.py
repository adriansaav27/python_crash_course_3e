usernames = ["admin", "username1", "username2", "username3", "username4"]
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")
