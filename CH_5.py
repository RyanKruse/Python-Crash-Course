# This chapter focuses on if-statements. Includes:
# logic (==, !=), and, or, in, is, is True, is False, not, if, else, elif,
# multiple ifs, if list, if empty list, if list A in list B,

# 5-1: ==
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car.lower() == 'audi')

# ==, and, or.
age = 23
print('\nIs my age equal to 23? ' + str(age == 23))
print('Is my age above 20 and below 30? ' + str((age > 20) and (age < 30)))
print('Am I older than 30 or younger than 25? ' + str((age > 30) or (age < 25)))

# in, and, or.
toppings = ['mushrooms', 'onions', 'pineapple']
print('\n' + str(toppings))
print('Is meat an available topping? ' + str('meat' in toppings))
print('Are onions, pineapple, or meat available? ' + str(('onions' or 'pineapple' or 'meat') in toppings))
print('Is meat and pineapple both available? ' + str(('meat' in toppings) and ('pineapple' in toppings)))

# is, is True, is False, not.
this_is_True = True
this_is_False = False
game_active = this_is_True
print('\nIs this_is_True a bool? ' + str(this_is_True is bool) + ' <-- ?')  # This is not correct.
print('Is this_is_True a bool that is true? ' + str(this_is_True is True))
print('Is this_is_False a bool that is false? ' + str(this_is_False is False))
print('Is this_is_False a bool that is true? ' + str(this_is_False is True))
print('Are one of the bool above not true? ' + str((this_is_False or this_is_True) is not True))

# 5-2: Logic.
bmw = 'bmw'
BMW = 'BMW'
print('\nHere are some mathematical statements being tested:')
print(bmw == BMW)
print(bmw == BMW.lower())
print(5 == 10)
print(5 != 10)
print(5 > 10)
print(5 < 10)
print(10 >= 10)
print(10 <= 10)

# 5-3: if.
alien_color = 'green'
if alien_color == 'green':
    print('\nYou have just earned 5 points.')

# 5-4: else.
alien_color = 'yellow'
if alien_color == 'green':
    print('You have just earned 5 points.')
else:
    print('You have just earned 10 points.')

# 5-5: elif.
alien_color = 'red'
if alien_color == 'green':
    print('You have just earned 5 points.')
elif alien_color == 'yellow':
    print('You have just earned 10 points.')
elif alien_color == 'red':
    print('You have just earned 15 points.')

# 5-6: if, elif, else.
age = 78
print('\nYour age is ' + str(age) + ' which means...')
if age < 2:
    print('You are a baby.')
elif (age >= 2) and (age < 4):
    print('You are a toddler.')
elif (age >= 4) and (age < 13):
    print('You are a kid.')
elif (age >= 13) and (age < 20):
    print('You are a teenager.')
elif (age >= 20) and (age < 65):
    print('You are an adult.')
else:
    print('You are an elder.')

# 5-7: Multiple ifs.
favorite_fruits = ['apples', 'oranges', 'pineapples']
print('\n' + str(favorite_fruits))
if 'bananas' in favorite_fruits:
    print('You like bananas!')
if 'strawberries' in favorite_fruits:
    print('You like strawberries!')
if 'apples' in favorite_fruits:
    print('You like apples!')
if 'oranges' in favorite_fruits:
    print('You like oranges!')
if 'pineapples' in favorite_fruits:
    print('You like pineapples!')

# 5-8: if list. 5-9: if empty list.
usernames = ['hipskovik', 'sassafrass', 'deershark', 'firebolt', 'admin']
# usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Greetings, ' + user.title() + ' thank you for logging in!')
else:
    print('We need to find some users!')

# 5-10: if list A in list B.
current_users = ['hipskovik', 'sassafrass', 'codaflash', 'firebolt', 'jova']
new_users = ['Codaflash', 'JOVA', 'phantom', 'mike', 'melo']
print('\nCurrent users: ' + str(current_users))
print('New users: ' + str(new_users))

for user in new_users:
    if user.lower() in current_users:
        print('\t' + user.title() + ', this username is not available. Please try a different one.')
    else:
        print('\t' + user.title() + ', this username is available.')

# 5-11: Multiple ifs.
numbers = list(range(1, 10))
print('\nList: ' + str(numbers))

for number in numbers:
    if number == 1:
        print('\t' + str(number) + 'st')
    elif number == 2:
        print('\t' + str(number) + 'nd')
    elif number == 3:
        print('\t' + str(number) + 'rd')
    else:
        print('\t' + str(number) + 'th')

# 5-12: Review styling.

# 5-13:
# So some ideas about different problems I would like to explore as a programmer would be the following:
# Create a tic tac toe game where the player is playing on a time limit against an AI.
# Create a tic tac toe game where the pieces are invisible.
# No web development, not interested unless its to display an AI game where others can play it.
# Might be interesting to see if AI has any use in data. I like working in data.
