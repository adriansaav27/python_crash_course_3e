sandwich_orders = [
    "pastrami",
    "BLT sándwich",
    "Reuben",
    "pastrami",
    "Sándwich de roast beef",
    "Croque-monsieur",
    "Cheesesteak",
    "pastrami",
]
finished_sandwiches = []

print("We have to finish the pastrami sandwiches!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
