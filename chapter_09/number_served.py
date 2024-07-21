class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Restaurant Pino Prestanizzi", "Italian")
print(f"Number of customers the restaurant has served: {restaurant.number_served}")
restaurant.set_number_served(9)
print(f"Number of customers the restaurant has served: {restaurant.number_served}")
restaurant.increment_number_served(2)
print(f"Number of customers the restaurant has served: {restaurant.number_served}")
