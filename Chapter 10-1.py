# 10-1: Reading an entire file, looping through a file, and storing lines in a list.
# 10-2: Use the replace method to replace all instances of 'Python' with another language.

# Reading an entire file.
with open('learning_python.txt') as file_python:
    print(file_python.read().replace('Python', 'C#'))

# Looping through each line.
with open('learning_python.txt') as file_python:
    for line in file_python.readlines():
        print(line.strip().replace('Python', 'C#'))

# Storing lines in a list.
with open('learning_python.txt') as file_python:
    line_list = []
    for line in file_python.readlines():
        line_list.append(line.replace('Python', 'C#'))
for element in line_list:
    print(element.strip())

# Bonus: Storing lines in a string.
with open('learning_python.txt') as file_python:
    line_str = ''
    for line in file_python.readlines():
        line_str += line.strip().replace('Python', 'C#')
    print(line_str)

# 10-3: Write a text document.
with open('guest.txt', 'w') as file_guest:
    guest = input('\nWhat is your name? ')
    file_guest.write(guest)

# 10-4: Write a text document that appends inputs.
with open('guest_book.txt', 'a') as file_guest_book:
    while True:
        guest = input('What is your name? (q to quit): ')
        if guest == 'q':
            break
        print('Welcome ' + guest.title())
        file_guest_book.write(guest + '\n')

# 10-5: Write a text document that appends inputs.
with open('like_programming.txt', 'a') as file_like_programming:
    while True:
        reason = input('Why do you like programming? (q to quit): ')
        if reason == 'q':
            break
        file_like_programming.write(reason + '\n')