# from printing_functions import User  #9-12: I have confirmed that this works for double imports.


class Restaurant():  # 9-10: Show I can import this code into another sheet.
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


class User():  # 9-11: Import this into another python script and show it works correctly.
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