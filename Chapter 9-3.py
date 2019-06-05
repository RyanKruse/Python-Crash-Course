from collections import OrderedDict
from random import randint

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

# 9-15: Unable to perform this task as I have no internet in my apartment.
