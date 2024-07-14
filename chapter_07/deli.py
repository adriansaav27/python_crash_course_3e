sandwich_orders = [ "BLT sándwich", "Reuben", "Sándwich de roast beef", "Croque-monsieur", "Cheesesteak" ]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)