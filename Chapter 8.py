# This chapter focuses on functions. The practice questions are attached to each function.
from import_functions import make_car as mc  # Uses an alias to prevent overlapping with same function names
import import_functions as pf  # Imports the entire module under an alias


def display_message():  # 8-1
    """Prints what I am learning in this chapter."""
    print('I am learning about functions, modules, and passing information in this chapter.')


display_message()


def favorite_book(title):  # 8-2
    """Prints my favorite book"""
    print('My favorite book is ' + title)


favorite_book('7 Habits of Highly Effective People')


def make_shirt(size, text):  # 8-3
    """Prints a shirt and message on that shirt."""
    print('The size of the shirt is a ' + size + ' and the message is ' + text + '.')


make_shirt('large', 'Hello world!')  # Positional argument.
make_shirt(text='Hello world!', size='large')  # Keyword argument.


def make_shirt2(size='large', text='I love Python'):  # 8-4
    """Prints a shirt and message on that shirt. Default value is large, 'I love Python'."""
    print('The size of the shirt is a ' + size + ' and the message is ' + text + '.')


make_shirt2()  # Default argument.
make_shirt2(size='medium')
make_shirt2(size='small', text='I love solving problems')


def describe_city(city, country='America'):  # 8-5
    """Prints a city in a country. Default value is America."""
    print(city.title() + ' is in ' + country.title() + '.')


describe_city('Seattle')
describe_city('new york')
describe_city('paris', 'france')


def city_country(city, country):  # 8-6
    """Returns a string of a city and country concatenated."""
    return city.title() + ', ' + country.title()


print(city_country('tokyo', 'japan'))
print(city_country('mexico city', 'mexico'))
print(city_country('havana', 'cuba'))


def make_album(artist_name, album_title, track_count=''):  # 8-7
    """Returns a dictionary of an album's artist, title, and track count (optional)."""
    album = {
        'artist': artist_name.lower(),
        'title': album_title.lower()
    }
    if track_count:
        album['tracks'] = track_count
    return album


print(make_album('jimmy hendrix', 'going home'))
print(make_album('pink floyd', 'dark side of the moon'))
print(make_album('the beatles', 'abby road'))
print(make_album('pink floyd', 'animals', '5'))


while True:
    artist_name = input("Enter an artist name. Enter 'q' to quit at any time: ")
    if artist_name == 'q':
        break
    album_title = input("Enter an album title: ")
    if album_title == 'q':
        break
    track_count = input("Enter a track count (optional): ")
    if track_count == 'q':
        break
    print('Your album is: ' + str(make_album(artist_name, album_title, track_count)) + '\n')


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

# 8-17: Follows the styling guidelines on this chapter.



