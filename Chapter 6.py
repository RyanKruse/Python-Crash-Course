# This chapter focuses on dictionaries. Includes:
# Keys, values, items, add, delete, bold, sets
# if list A in dict B, list of dicts, list in dicts, dict of dicts

# 6-1.
person = {'first_name': 'jeff', 'last_name': 'bezos', 'age': '54', 'city': 'seattle'}
print('First name is ' + str(person['first_name'].title()) + '.')
print('Last name is ' + str(person['last_name'].title()) + '.')
print('Age is ' + str(person['age']) + '.')
print('City of residency is ' + str(person['city'].title()) + '.')

# 6-2.
names = ['chris', 'john', 'ryan', 'kaitlyn', 'austen']
favorites = {'chris': 40, 'john': 25, 'ryan': 15, 'kaitlyn': 42, 'austen': 64}
print("\nI have a list of people. Here are their favorite numbers!")
for name in names:
    print('\t' + name.title() + "'s favorite number is " + str(favorites[name]) + '.')

# 6-3.
words = ['list', 'tuple', 'for-loop', 'if-statement', 'print']
definitions = {
    'list': 'A list is basically an array.',
    'tuple': 'A tuple is basically a fixed array.',
    'for-loop': 'A for-loop will loop based on the number of indexes or range.',
    'if-statement': 'An if-statement checks if something is True or False.',
    'print': 'A print statement will print text into the console.'
}
print('\nHere are 5 programming definitions I wrote!')
for index, word in enumerate(words, start=1):
    print('\t' + str(index) + ') ' + word.title() + ': ' + definitions[str(word)])

# 6-1 Transformed to Dictionary.
person = {'first_name': 'jeff', 'last_name': 'bezos', 'age': '54', 'city': 'seattle'}
for key, value in person.items():
    print(key.title() + ': ' + value.title() + '.')

# 6-2 Transformed to Dictionary.
favorites = {'chris': 40, 'john': 25, 'ryan': 15, 'kaitlyn': 42, 'austen': 64}
print("\nHere are these people's favorite numbers!")
for key, value in favorites.items():
    print('\t' + key.title() + "'s favorite number is " + str(value) + ".")

# 6-3 Transformed to Dictionary.
definitions = {
    'list': 'Basically an array. Can add, change, and remove elements.',
    'tuple': 'Basically a fixed array. Cannot add, change, or remove elements.',
    'for-loop': 'The for-loop loops based on the list or range used.',
    'if-statement': 'Checks if something is True or False.',
    'print': 'Will print text into the console.',
    'dictionary': 'Stores keys and values. Both can be pulled by items().',
    'sort': 'Sorts a list. This can be a temporary or permanent sort.',
    'slice': 'Works with part of a list to loop or copy it.',
    'range': 'Used to specify a list of numbers or loop length.',
    'conditions': 'If-statements use these to determine True or False.'
}
print('\nHere are 10 programming definitions I wrote!')
for key, value in definitions.items():
    print('\t' + key.title() + ': ' + value)

# Add.
words = {'carrot': 'A carrot is a vegetable.'}
words['pineapple'] = 'A pineapple is a fruit.'

# Delete.
del words['carrot']

# Bold text.
print('\nHello!\t\033[1m This text is bold!\033[0m \tAnd this text is normal!')

# 6-5: Only key, only value.
rivers = {
    'nile': 'egypt',
    'mississippi': 'america',
    'amazon': 'brazil'
}
for key, value in rivers.items():
    print('The ' + key.title() + ' River is located in ' + value.title() + '.')
print('\nThese are the keys in the dictionary:')
for key in rivers.keys():
    print('\t' + key.title())
print('\nThese are the values in the dictionary:')
for value in rivers.values():
    print('\t' + value.title())

# 6-6: if list A in dict B.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
names = ['sarah', 'jimmy', 'edward', 'mallory']
print('')
for name in names:
    if name in favorite_languages.keys():
        print('Hello ' + name.title() + ', thank you for taking the poll.')
    else:
        print('Hello ' + name.title() + ', you are invited to take the poll.')

# Sets
print('')
for value in set(favorite_languages.values()):
    print(value.title() + ' was a language mentioned.')

# 6-7: List of dictionaries.
person_0 = {'first_name': 'jeff', 'last_name': 'bezos', 'age': '54', 'city': 'seattle'}
person_1 = {'first_name': 'warren', 'last_name': 'buffet', 'age': '87', 'city': 'omaha'}
person_2 = {'first_name': 'sam', 'last_name': 'walton', 'age': '74', 'city': 'kingfisher'}
people = [person_0, person_1, person_2]
print('')
for person in people:
    print(person['first_name'] + ' ' + person['last_name'] + ' is ' + person['age'] +
          ' years old and lives in ' + person['city'] + '.')

# 6-8: List of dictionaries.
dog = {'corgie': 'john'}
fish = {'tuna': 'samantha'}
cat = {'tabby': 'jessica'}
pets = [dog, fish, cat]
print('')
for index, pet in enumerate(pets, start=1):
    for key, value in pet.items():
        if key == 'tuna':
            print('\t' + str(index) + ') ' + value.title() + "'s pet is a " + key + '. Who keeps a tuna as a pet?')
        else:
            print('\t' + str(index) + ') ' + value.title() + "'s pet is a " + key + '.')

# 6-9: List in dictionary.
favorite_places = {
    'john': ['paris', 'rome', 'london'],
    'samantha': ['singapore', 'tokyo'],
    'jessica': ['chicago', 'boston', 'san diego']
}
print('')
for key, value in favorite_places.items():
    print(key.title() + "'s favorite places are:")
    for index, place in enumerate(value, start=1):
        print('\t' + str(index) + ') ' + place.title())

# 6-10: List in dictionary.
favorites = {
    'chris': [40, 60, 80],
    'john': [15, 24, 81, 95],
    'samantha': [39],
    'jessica': [42, 66],
    'bob': [64, 68]
}
print('\nHere are some favorite numbers!')
for key, value in favorites.items():
    print(key.title() + "'s favorite numbers are...")
    for number in value:
        print(number)

# 6-11: Dictionary of dictionaries.
cities = {
    'new york': {
        'country': 'america',
        'population': 18000000,
        'fact': 'It was founded in 1650.'
    },
    'tokyo': {
        'country': 'japan',
        'population': 30000000,
        'fact': 'It is the capital of Japan.'
    },
    'london': {
        'country': 'the united kingdom',
        'population': 12000000,
        'fact': 'It has a lot of museums.'
    }
}
print('')
for city, city_info in cities.items():
    print(city.title() + ' is in ' + city_info['country'].title() + ' with a population of ' +
          str(city_info['population']) + '. ' + city_info['fact'])

# 6-12: Already completed with # 6-8.
