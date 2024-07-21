class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def flavors_list(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


restaurant = IceCreamStand("Ice Cream Summer", "Italian")
restaurant.flavors_list()
