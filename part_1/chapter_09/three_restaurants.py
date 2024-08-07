class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Type: {self.cuisine_type}")


restaurant = Restaurant("Restaurant Pino Prestanizzi", "Italian")
restaurant.describe_restaurant()
restaurant = Restaurant("ABaC", "Modern")
restaurant.describe_restaurant()
restaurant = Restaurant("Cenador de Amós", "Regional")
restaurant.describe_restaurant()
