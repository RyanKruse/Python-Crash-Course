from printing_classes import Admin as Admin_Import


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
