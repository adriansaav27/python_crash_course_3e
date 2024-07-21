class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")


# restaurant = Restaurant("Restaurant Pino Prestanizzi", "Italian")
# print(f"Attribute 'restaurant_name': {restaurant.restaurant_name}")
# print(f"Attribute 'cuisine_type': {restaurant.cuisine_type}")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
