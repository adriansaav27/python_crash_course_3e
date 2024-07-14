while True:
    prompt = input("Hi! How old are you?\n")
    
    if int(prompt) < 3:
        print("The cost is FREE")
    elif int(prompt) >= 3 and int(prompt) < 12:
        print("The cost is $10")
    else:
        print("The cost is $15")