def sandwitch_items(*items):
    for item in items:
        print(f">>> {item}")
    print("\n")


sandwitch_items("cheese")
sandwitch_items("lettuce", "tomato", "cheese")
sandwitch_items("lettuce", "cheese")
