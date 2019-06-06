# This chapter focuses on inputs. Includes:
# int(), remainder, break, active variable, increment, continue, sets, pop, append, keys, values

# 7-1: Input.
car = input('Enter the rental car would you like: ')
print('Okay, the ' + car.title() + ' sedan is available!')

# 7-2: str to int.
people = input('Enter the number of people in your dinning group (use integers): ')
people = int(people)
if people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print('We have a table available for you.')

# 7-3: Remainder.
number = input("Enter a number and we'll check if it's a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + ' is a multiple of 10.')
else:
    print(str(number) + ' is not a multiple of 10.')

# 7-4: Append inputs.
prompt = '\nEnter a pizza topping and I will add it on.'
prompt += "\n(Enter 'quit' to exit): "
all_toppings = []
while True:
    topping = input(prompt)
    if topping == 'quit':
        print('All done! The toppings we have on your pizza are: ' + str(all_toppings))
        break
    else:
        print('Okay, adding on ' + topping + '.')
        # Bonus Code:
        all_toppings.append(topping)
        print('The toppings we have now are: ' + str(all_toppings))

# 7-5: Break.
prompt = "\nEnter your age to get ticket price (enter 'quit' to exit): "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free.')
    elif age < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')

# 7-6: Active variable.
prompt = "\nEnter your height in feet (enter 'quit' or 'stop' to exit): "
active = True

while active:
    height = input(prompt)
    if height == 'quit':
        active = False
    elif height == 'stop':
        break
    else:
        height = int(height)
        if height < 3:
            print('You must be above 3 feet tall to ride this roller coaster.')
        else:
            print('You may now enter to ride this roller coaster.')

# 7-7: Infinite while-loop.
# number = 0
# while number < 5:
#     print(number)

# Increment.
number = 0
while number < 3:
    number += 1
    print(number)

# Continue.
number = 0
while number < 5:
    number += 1
    if number % 2 == 0:
        continue
    else:
        print(number)

# Sets.
pets = ['cat', 'cat', 'dog', 'cat', 'fish', 'bird', 'dog']
print('A list without any repetition of elements: ' + str(set(pets)) + '\n')

# 7-8: Pop and append list to list. 7-9: Remove all.
sandwich_orders = ['pastrami', 'rubio', 'subway', 'pastrami', 'bacon', 'pastrami']  # 7-9 (add x3 'pastrami')
sandwich_finished = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    sandwich_finished.append(sandwich)
    print('I made you a ' + sandwich + ' sandwich!')
print('Here are all the sandwiches made: ' + str(sandwich_finished))

# 7-10: Append dictionary keys and values. Enumerate, break, continue, counter.
responses = {}
number = 1

while True:
    value = input('\nWhat is your favorite programming language: ')
    key = input('You are person #' + str(number) + ' to take this poll. What is your name: ')
    active = input('Would you like to let another person take the poll (yes/no/redo): ')
    if active.lower() == 'redo':
        print('\t***REDOING THE PREVIOUS POLL INPUT***')
        continue
    responses[key] = value  # Adds user inputs to dictionary.
    if active.lower() == 'no':
        break
    number += 1

print('\n' + str(number) + ' people took the poll. Here are the results: ')
for index, (key, value) in enumerate(responses.items(), start=1):
    print('\t' + str(index) + ') ' + key.title() + "'s favorite programming language is " + value.title() + '.')
