from printing_classes import Restaurant as Restaurant_Import  # 9-10: Import and use a class.


class Restaurant():  # 9-1: Make a class. & 9-4: Add a number_served attribute and number_served methods.
    """Models a restaurant."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize name, cuisine attributes, and number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Prints restaurant name and cuisine type."""
        print('The restaurant is ' + self.restaurant_name + ' and serves ' + self.cuisine_type + ' cuisine.')

    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print('The restaurant is now open for business!')

    def set_number_served(self, set_number):
        """Sets the number served with a new number."""
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        """Increments the current number served"""
        self.number_served += increment_number


class IceCreamStand(Restaurant):  # 9-6: Ice cream stand problem.
    """A child class of restaurant class."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize attributes of the parent class.
        Then initializes an attribute (flavor) specific to the ice cream stand class."""
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'mint']

    def display_flavors(self):
        """Prints ice cream flavors."""
        print('This ice cream stand serves the following flavors: ')
        for index, flavor in enumerate(self.flavors, start=1):
            print('\t' + str(index) + ') ' + flavor.title() + '.')


# 9-1: Prints information about a restaurant.
my_restaurant = Restaurant('Red Lobster', 'seafood')
print('Restaurant Name: ' + my_restaurant.restaurant_name)
print('Cuisine Type: ' + my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9-2: Print different variants of the restaurant class.
print('')
joe_restaurant = Restaurant("Joe's Crab Shack", 'seafood')
jill_restaurant = Restaurant("Jill's Baking House", 'pastry')
chain_resturant = Restaurant("T.G.I. Friday's", 'American')

joe_restaurant.describe_restaurant()
jill_restaurant.describe_restaurant()
chain_resturant.describe_restaurant()

# 9-4: Modifies values in a class instance in 3 different ways.
restaurant = Restaurant('Pizza Planet', 'pizza')
print('\nThe number served after opening is: ' + str(restaurant.number_served))
restaurant.number_served = 27
print('The number served after breakfast is: ' + str(restaurant.number_served))
restaurant.set_number_served(75)
print('The number served after lunch is: ' + str(restaurant.number_served))
restaurant.increment_number_served(100)
print('The number served after dinner is: ' + str(restaurant.number_served))

# 9-6
print('')
ice_cream_stand = IceCreamStand('1 Dollar Ice Cream', 'ice cream')
ice_cream_stand.display_flavors()

# 9-10: Show imports on a class work.
print('')
yummy_restaurant = Restaurant_Import("Olive Garden", 'Italian')
yummy_restaurant.describe_restaurant()
yummy_restaurant.open_restaurant()
yummy_restaurant.set_number_served(25)
yummy_restaurant.increment_number_served(10)
print('The number served after lunch is: ' + str(yummy_restaurant.number_served))  # Is 35.
yummy_restaurant.cuisine_type = 'Americanized Italian'
yummy_restaurant.describe_restaurant()
