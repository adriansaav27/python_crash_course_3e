pizzas = [ 'napolitana', 'carbonara', 'margarita' ]
friend_pizzas = pizzas[:]
pizzas.append('hawaiana')
friend_pizzas.append('pepperoni')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)