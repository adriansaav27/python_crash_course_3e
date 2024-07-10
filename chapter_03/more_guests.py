guests = ['Ray', 'Andrew', 'Andra']
print(f'{guests[0]}, you are invited to the party!')
print(f'{guests[1]}, you are invited to the party!')
print(f'{guests[2]}, you are invited to the party!')
print(f'I found a bigger table :)')
guests.insert(0, 'George')
guests.insert(2, 'Axel')
guests.append('Maria')
print(f'Guests: {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]}, {guests[5]}')