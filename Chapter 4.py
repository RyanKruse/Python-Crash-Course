# This chapter focuses on for-loops. Includes:
# List, range, list(range) min, max, sum, odds, cubed, slicers, comprehension, duplicates, tuple, enumerates

# 4-1: For-loop list.
pizzas = ['pepperoni', 'cheesy', 'meaty']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza!')
print('Boy, I sure do love pizza.\n')

# 4-2: List.
pets = ['dog', 'cat', 'bunny']
for pet in pets:
    print('A ' + pet + ' would be a great pet.')
print('All of these animals would be great pets.')

# 4-3: Range.
for value in range(1, 21):
    print(value)

# 4-4: List and range.
hundred = list(range(1, 101))
for value in hundred:
    print(value)

# List comprehension.
ten = [print(value) for value in range(1, 11)]

# 4-5: Min, max, and sum.
print('\n' + str(min(hundred)) + ' is the smallest number in the array.')
print(str(max(hundred)) + ' is the largest number in the array.')
print(str(sum(hundred)) + ' is the sum of all 1 million numbers in the array.')

# 4-6: Odds
odds = list(range(1, 21, 2))
for value in odds:
    print(value)
print('')

# 4-7: Divisible by 3.
threes = list(range(3, 31, 3))
for value in threes:
    print(value)
print('')

# 4-8: Cubed.
cubed = []
for value in range(1, 11):
    cubed.append(value**3)
    print(value**3)
print('\n' + str(cubed) + ' by for loop.')

# 4-9: List comprehension.
cubed = list(value**3 for value in range(1, 11))
print(str(cubed) + ' by list comprehension.')

# 4-10: Slicers.
print('The first three items in the cubed list are: ' + str(cubed[0:3]))
print('Three items from the middle of the cubed list are: ' + str(cubed[3:7]))
print('The last three items in the cubed list are: ' + str(cubed[-3:]))

# 4-11: Duplicates.
pizzas = ['pepperoni', 'cheesy', 'meaty']
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('pineapple')

# Prove duplicate lists.
print('\nMy favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
print('')

# 4-12: List.
favorites = ['pizza', 'falafel', 'carrot cake', 'cannoli']
for favorite in favorites:
    print('One of my favorite foods is ' + favorite + '.')
print('')

# 4-13: Tuple and enumerate.
foods = ('pasta', 'pizza', 'french fries', 'hamburgers', 'hot dogs')
# foods[2] = 'noodles'  # error
print('This restaurant buffet offers: ')
for index, food in enumerate(foods, start=1):
    print('\t' + str(index) + ') ' + food.title())

# Replace tuple.
foods = ('pasta', 'salad', 'french fries', 'hamburgers', 'noodles')
print('\nChanging the menu, this restaurant buffet offers: ')
for index, food in enumerate(foods, start=1):
    print('\t' + str(index) + ') ' + food.title())

# 4-14: PEP 8 Style Guide (https://python.org/dev/peps/pep-0008)

# 4-15: Apply code review.
