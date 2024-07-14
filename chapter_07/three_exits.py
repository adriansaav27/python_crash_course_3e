cont = 0
while True:
    cont += 1
    prompt = input("Hi! How old are you? (Enter 'quit' when you are finished.)\n")
    
    if prompt == 'quit':
        break
    
    if int(prompt) < 3:
        print("The cost is FREE")
    elif int(prompt) >= 3 and int(prompt) < 12:
        print("The cost is $10")
    else:
        print("The cost is $15")

print(f"It has been asked {cont} times")