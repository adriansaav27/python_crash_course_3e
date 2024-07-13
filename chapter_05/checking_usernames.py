current_users = [ 'User1', 'User2', 'User3', 'User4', 'User5' ]
current_users_copy = [ item.lower() for item in current_users ]
new_users = [ 'user6', 'user2', 'user7', 'user4', 'user8' ]

for user in new_users:
    if user in current_users_copy:
        print(f'Username "{user}" is unavailable')
    else:
        print(f'Username "{user}" is available')