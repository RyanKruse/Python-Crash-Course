# This chapter focuses on lists. Includes:
# index, append, insert, delete, remove, pop, sort, sorted, reverse, last, length, comprehension

# 3-1: List index.
names = ['Tyler', 'Rachel', 'Hector']
print(names[0])
print(names[1])
print(names[2])

# 3-2: List index and string.
print('Hello ' + names[0] + ', it is nice meeting you.')
print('Hello ' + names[1] + ', it is nice meeting you.')
print('Hello ' + names[2] + ', it is nice meeting you.')

# 3-3: Title and upper case.
favorite_transportation = ['toyota', 'bmw', 'audi']
print('\nI would like to drive a cheap ' + favorite_transportation[0].title() + ' to work.')
print('I would like to own an expensive ' + favorite_transportation[1].upper() + ' car when I am older.')
print('I think ' + favorite_transportation[2].title() + ' cars are too expensive for me right now.')

# 3-4: List index.
guests = ['John', 'Robert', 'Sam']
print('\n' + guests[0] + ' is invited to dinner.')
print(guests[1] + ' is invited to dinner.')
print(guests[2] + ' is invited to dinner.')

# 3-5: Remove and insert.
print('\nActually... ' + guests[1] + ' cannot make it to dinner. Jimmy will replace him.')
guests.remove('Robert')
guests.insert(1, 'Jimmy')
print(guests[0] + ' is invited to dinner.')
print(guests[1] + ' is invited to dinner.')
print(guests[2] + ' is invited to dinner.')

# 3-6: Insert and append.
print('\nOh my, I found a bigger dinner table to hold 6 people instead. Let us invite 3 more people.')
guests.insert(0, 'Hanna')
guests.insert(2, 'Jill')
guests.append('Morgana')
print(guests[0] + ' is invited to dinner.')
print(guests[1] + ' is invited to dinner.')
print(guests[2] + ' is invited to dinner.')
print(guests[3] + ' is invited to dinner.')
print(guests[4] + ' is invited to dinner.')
print(guests[5] + ' is invited to dinner.')

# 3-7: Pop.
print('\nOops. The table never arrived so we only have a coffee table now. I only have space for 2 people.')
uninvited = guests.pop(0)
print('Sorry ' + uninvited + ', we have to remove you.')
uninvited = guests.pop(0)
print('Sorry ' + uninvited + ', we have to remove you.')
uninvited = guests.pop(0)
print('Sorry ' + uninvited + ', we have to remove you.')
uninvited = guests.pop(0)
print('Sorry ' + uninvited + ', we have to remove you.')
print(guests[0] + ' you are still invited.')
print(guests[1] + ' you are still invited.')

# Delete.
del guests[0]
del guests[0]
print('\nActually, nobody is invited. I caught the flu! The guest list array looks like this: ' + str(guests))

# 3-8: Temporarily sort.
locations = ['Paris', 'Rome', 'Tokyo', 'Chicago', 'Los Angles']
print('\n' + str(locations) + ' Normal')
print(str(sorted(locations)) + ' Temporarily Sorted')

# Temporarily reverse-sort.
print(str(locations) + ' Normal')
print(str(sorted(locations, reverse=True)) + ' Temporarily Reverse Sorted')
print(str(locations) + ' Normal')

# Permanently reverse.
locations.reverse()
print(str(locations) + ' Permanently Reversed')
locations.reverse()
print(str(locations) + ' Permanently Reversed (again)')

# Permanently sort.
locations.sort()
print(str(locations) + ' Permanently Sort')

# Permanently reverse-sort.
locations.sort(reverse=True)
print(str(locations) + ' Permanently Reverse Sort')

# 3-9 Length.
print('\nExamining the length of the list of dinner guests, I am inviting ' + str(len(guests)) + ' guests.')
print("Examining the length of the list of locations, I have " + str(len(locations)) + " locations")

# 3-10.
# Titled, upper, and lower.
Maps = ['castlwars', 'Rooftops', 'ORBITZ', 'sp00nage', 'melon fields']
print('\nI have a list of Sassilization maps: ' + str(Maps))
print(Maps[0] + ' titled is: ' + Maps[0].title())
print(Maps[1] + ' upper-cased is: ' + Maps[1].upper())
print(Maps[2] + ' lower-cased is: ' + Maps[2].lower())

# Last element.
print('The last element accessed by Maps[3]: ' + Maps[4])
print('The last element accessed by Maps[-1]: ' + Maps[-1])

# Replace, append, and delete.
Maps[0] = 'castlebase'
print('\nReplace castlwars with castlebase: ' + str(Maps))
Maps.append('Hidden Temple')
print('Append Hidden Temple to the end of the map list: ' + str(Maps))
del Maps[2]
print('Delete ORBITZ by index from the map list: ' + str(Maps))

# Pop last and pop index.
popped = Maps.pop()
print('\nPopping ' + popped + ' by variable yields: ' + str(Maps))
print('Popping ' + Maps.pop() + ' in the same print statement yields: ' + str(Maps))
print('Popping ' + Maps.pop(1) + ' by element yields: ' + str(Maps))

# Remove.
remove_map = 'sp00nage'
Maps.remove(remove_map)
print('Remove ' + remove_map + ' from the map list by variable and string: ' + str(Maps))

# Temp sort and reverse-sort.
Maps = ['castlwars', 'rooftops', 'orbitz', 'sp00nage', 'melon fields']
print("\nOriginal map list in lowercase: " + str(Maps))
print("Sorting temporarily: " + str(sorted(Maps)))
print("Reverse sorting temporarily: " + str(sorted(Maps, reverse=True)))

# Permanent sort and reverse-sort.
Maps.reverse()
print('Reverse the list: ' + str(Maps))
Maps.sort()
print('Sort permanently: ' + str(Maps))
Maps.sort(reverse=True)
print('Reverse sort permanently: ' + str(Maps))

# Length.
print('\nThe length of the map list above is: ' + str(len(Maps)))

# 3-11: Index error.
# Maps = []
# print(Maps[-1])
