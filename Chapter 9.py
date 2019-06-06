# This chapter focuses on classes. The problem number is attached to each class/function.
from import_classes import Restaurant as Restaurant_Import  # 9-10: Import and use a class.
from import_classes import Admin as Admin_Import
from collections import OrderedDict
from random import randint


class Restaurant:  # 9-1: Make a class. & 9-4: Add a number_served attribute and number_served methods.
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


class User():  # 9-3: Make a user class. 9-5: Add a login_attempts attribute and then methods.
    """Models a user."""
    def __init__(self, first_name, last_name, gender, age, login_attempts=0):
        """Stores user information."""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        """Prints information about the user."""
        print(self.first_name.title() + ' ' + self.last_name.title()
              + ' is a ' + self.gender + ' aged ' + str(self.age) + '.')

    def greet_user(self):
        """Prints a welcoming message to the user."""
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        """Increments login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login_attempts"""
        self.login_attempts = 0


class Admin(User):
    """A child class of the parent class User."""
    def __init__(self, first_name, last_name, gender, age, login_attempts=0):
        """Initialize attributes of the parent class.
        Then initializes an attribute (privileges) specific to the Admin class."""
        super().__init__(first_name, last_name, gender, age, login_attempts)
        self.privileges = Privileges()  # This is a class. Make sure to add the () at the end.


class Privileges():
    """Contains the privileges for the Admin class."""
    def __init__(self, reputation=500, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges
        self.reputation = reputation

    def show_privileges(self):
        """Print the privileges that the Admin class has."""
        print('The admin has the following privileges: ' + str(self.privileges))

    def show_reputation(self):
        """Print the reputation that the Admin class has."""
        print('The admin has the following reputation: ' + str(self.reputation))
        if self.reputation > 800:
            print('\tThis admin is popular!')

    def set_reputation(self, new_reputation):
        """Upgrades the reputation that the Admin class has based on input."""
        max_reputation = 999
        min_reputation = 0
        if new_reputation > max_reputation:
            self.reputation = max_reputation
        elif new_reputation < min_reputation:
            self.reputation = min_reputation
        else:
            self.reputation = new_reputation


user1 = User('john', 'smith', 'male', 29)
user2 = User('rebbecca', 'goldberg', 'female', 45)
user3 = User('mary', 'doe', 'female', 67)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# 9-5: Test to see if login_attempt methods work using user1.
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print('\nCurrent login attempts: ' + str(user1.login_attempts))

user1.reset_login_attempts()
print('Current login attempts: ' + str(user1.login_attempts))

# 9-7: Calls the child class method.
print('')
phantom = Admin('george', 'thomson', 'male', 29)
# phantom.show_privileges()
# This line became obsolete from exercise 9-8; moving show_privileges out of Admin and into Privileges.

# 9-8: Call the child class method privileges.
phantom.privileges.show_privileges()

# 9-9: Use methods to modify values in a child class parameter. Substitute for Tesla example.
phantom.privileges.show_reputation()

phantom.privileges.set_reputation(-500)
phantom.privileges.show_reputation()

phantom.privileges.set_reputation(2500)
phantom.privileges.show_reputation()

phantom.privileges.set_reputation(777)
phantom.privileges.show_reputation()

# 9-11: Show that imports work correctly for classes and child classes.
print('')
Sassafrass = Admin_Import('greg', 'harrison', 'male', 32)
Sassafrass.describe_user()
Sassafrass.greet_user()
Sassafrass.privileges.show_privileges()

# 9-12: Show that double imports (i.e. import module into another module into a script) works. It worked.

# 9-13: Print keys and values from a dictionary in the order they were added in using OrderedDict.
definitions = OrderedDict()

definitions['list'] = 'Basically an array. Can add, change, and remove elements.'
definitions['tuple'] = 'Basically a fixed array. Cannot add, change, or remove elements.'
definitions['for-loop'] = 'The for-loop loops based on the list or range used.'
definitions['if-statement'] = 'Checks if something is True or False.'
definitions['print'] = 'Will print text into the console.'
definitions['dictionary'] = 'Stores keys and values. Both can be pulled by items().'
definitions['sort'] = 'Sorts a list. This can be a temporary or permanent sort.'
definitions['slice'] = 'Works with part of a list to loop or copy it.'
definitions['range'] = 'Used to specify a list of numbers or loop length.'
definitions['conditions'] = 'If-statements use these to determine True or False.'

print('\nHere are 10 programming definitions I wrote!')
for index, (key, value) in enumerate(definitions.items(), start=1):
    print('\t' + str(index) + ')\t' + key.title() + ': ' + value)


class Die():  # 9-14: Do random dice stuff.
    """Die class which contains by default 6 sides."""
    def __init__(self, sides=6):
        """Sets up variables"""
        self.sides = sides

    def roll_die(self):
        """This rolls the die"""
        print('The die (' + str(self.sides) + ' sided) rolled: ' + str(randint(1, self.sides)))


Dice_6 = Die()
for value in range(1, 11):
    Dice_6.roll_die()

Dice_10 = Die(10)
for value in range(1, 11):
    Dice_10.roll_die()

Dice_20 = Die(20)
for value in range(1, 11):
    Dice_20.roll_die()
