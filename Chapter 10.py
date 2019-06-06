# This chapter focuses on reading and writing to files.
# 10-1: Reading an entire file, looping through a file, and storing lines in a list.
# 10-2: Use the replace method to replace all instances of 'Python' with another language.
import json

# Reading an entire file.
with open('text_files/learning_python.txt') as file_python:
    print(file_python.read().replace('Python', 'C#'))

# Looping through each line.
with open('text_files/learning_python.txt') as file_python:
    for line in file_python.readlines():
        print(line.strip().replace('Python', 'C#'))

# Storing lines in a list.
with open('text_files/learning_python.txt') as file_python:
    line_list = []
    for line in file_python.readlines():
        line_list.append(line.replace('Python', 'C#'))
for element in line_list:
    print(element.strip())

# Bonus: Storing lines in a string.
with open('text_files/learning_python.txt') as file_python:
    line_str = ''
    for line in file_python.readlines():
        line_str += line.strip().replace('Python', 'C#')
    print(line_str)

# 10-3: Write a text document.
with open('text_files/guest.txt', 'w') as file_guest:
    guest = input('\nWhat is your name? ')
    file_guest.write(guest)

# 10-4: Write a text document that appends inputs.
with open('text_files/guest_book.txt', 'a') as file_guest_book:
    while True:
        guest = input('What is your name? (q to quit): ')
        if guest == 'q':
            break
        print('Welcome ' + guest.title())
        file_guest_book.write(guest + '\n')

# 10-5: Write a text document that appends inputs.
with open('text_files/like_programming.txt', 'a') as file_like_programming:
    while True:
        reason = input('Why do you like programming? (q to quit): ')
        if reason == 'q':
            break
        file_like_programming.write(reason + '\n')

# 10-6: Catch an input error adds 2 numbers.
try:
    num_1 = int(input('This program adds 2 numbers. Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
except ValueError:
    print('Only enter numerical values.')
else:
    print(num_1 + num_2)

# 10-7: Write the above code in a while loop.
counter = 0
while True:
    try:
        num = input('I add numbers, [' + str(counter) + ']: (q to quit) ')
        if num == 'q':
            break
        num = int(num)
    except ValueError:
        print('Only enter numerical values.')
    else:
        counter += num


# 10-8: Print the lines of a list of files. 10-9: Silently fail is file was not found.
def print_contents(file_names):
    for file_name in file_names:
        try:
            with open(file_name) as file_opened:
                contents = file_opened.read()
        except FileNotFoundError:
            print('File name ' + file_name + ' was not found.')
            pass
        else:
            print(contents)


pets = ['text_files/cats.txt', 'text_files/birds.txt', 'text_files/dogs.txt']
print_contents(pets)


# 10-10: Count how many times a word appears in a txt file.
def count_words(file_name, word):
    with open(file_name) as file_opened:
        content = file_opened.read().lower()
        word_count = content.count(word.lower())
        print('The word ' + word + ' appears ' + str(word_count) + ' times.')


count_words('text_files/blog_post.txt', 'Sassilization')


# 10-11: Use JSON to write and receive information in a file. 10-12: Make it more complex.
def get_stored_number():
    try:
        with open('text_files/favorite_number.json') as j_obj:
            fav_num = json.load(j_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def get_new_number():
    fav_num = input('What is your favorite number? ')
    with open('text_files/favorite_number.json', 'w') as j_obj:
        j_obj.write(fav_num)


def favorite_number():
    """Stores a user's favorite number in JSON or retrieves it"""
    fav_num = get_stored_number()
    if fav_num:
        print('Your favorite number is ' + str(fav_num) + '.')
        change = input('Would you like to change it? (y/n) ')  # 10-13
        if change == 'y':
            get_new_number()
    else:
        get_new_number()


favorite_number()

# 10-13: Did this with favorite number.
