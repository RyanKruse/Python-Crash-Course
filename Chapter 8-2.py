from printing_functions import make_car as mc  # Uses an alias to prevent overlapping with same function names
import printing_functions as pf  # Imports the entire module under an alias


def show_magicians(names):  # 8-9
    """Prints all the person's names in a list."""
    for person in names:
        print("Hello, " + person.title() + "!")


def make_great(names, great):  # 8-10
    """Copies a list into another list, concatenating a string onto each element."""
    while names:
        temp = names.pop()
        great.append(temp + ' the Great')


# 8-9
names = ['hudini', 'david', 'michael']
great = []
show_magicians(names)

# 8-10
make_great(names, great)
show_magicians(great)

# 8-11: Does the same as above except doesn't change original list.
names = ['hudini', 'david', 'michael']
great = []
make_great(names[:], great)
show_magicians(names)
show_magicians(great)


def sandwich(*toppings):  # 8-12
    """Prints a list of any number of toppings on a sandwich"""
    print('The sandwich has the following toppings:')
    for index, topping in enumerate(toppings, start=1):
        print('\t' + str(index) + ') ' + topping.title())


sandwich('mushroom')
sandwich('pepperoni', 'salami', 'swiss')
sandwich('lettus', 'tomato', 'bacon')


def build_profile(first, last, **user_info):  # 8-13: user_info is in items format; requires for-loop.
    """Builds a dictionary containing everything we know about a user's profile."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():  # This takes arbitrary keyword arguments.
        profile[key] = value
    return profile


user_profile = build_profile('john', 'doe', major='economics', field='health care',
                             hobbies=['reading books', 'programming', 'going outside'])
print(user_profile)


def make_car(manufacturer, model, **car_info):  # 8-14
    """Builds a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('bmw', '3 series', color='blue', convertable='true', hybrid='true', cost=120000)
print(car)

# 8-15: Use the code in 8-13 and print it from a module.
car = mc('subaru', 'sedan', color='silver', convertable='false', hybrid='true', cost=40000)
print(car)

# 8-16: Use the code in 8-7 and print it from a module.
album = pf.make_album('the beatles', 'abby road', 9)
print(album)

# 8-17: Follow the styling guidelines on this chapter.
