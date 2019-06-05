# We are in function territory. The practice questions are attached to each function.
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
describe_city('paris','france')


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




