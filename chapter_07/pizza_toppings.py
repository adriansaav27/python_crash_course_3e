while True:
    prompt = input(
        "Enter the pizza ingredients :) (Enter 'quit' when you are finished.)\n"
    )

    if prompt == "quit":
        break

    print(f"You have added: {prompt}")
