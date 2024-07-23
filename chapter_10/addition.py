firts_num = 0
second_num = 0

while True:
    try:
        firts_num = int(input("Enter the firts number: "))
        break
    except:
        print(f"'Is not a number!")

while True:
    try:
        second_num = int(input("Enter the second number: "))
        break
    except:
        print(f"'Is not a number!")

print(f"The first and second values are numbers")
