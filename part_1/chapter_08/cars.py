def make_car(manufacturer, model_name, **characteristics):
    characteristics["model_name"] = model_name
    characteristics["manufacturer"] = manufacturer
    return characteristics


car = make_car("outback", "subaru", color="blue", tow_package=True)

for key, value in car.items():
    print(f"{key} -> {value}")
