vacations = []

while True:
    prompt = input(
        "If you could visit a place in the world, where would you go? (Enter 'quit' when you are finished.)\n"
    )

    if prompt == "quit":
        break

    vacations.append(prompt)

print(vacations)
