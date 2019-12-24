lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# add a list to a list
# friends.extend(lucky_numbers)
# print(friends)

# add individual entry to the end of a list
friends.append("Creed")

# add individual entry to middle of list. Index number to insert and the value to enter
friends.insert(1, "Kelly")
# print(friends)

# remove entry from a list
# friends.remove("Jim")
# print(friends)

# wipe a list
#friends.clear()

# remove last entry to a list
# friends.pop()
# print(friends)

# look for an entry in a list, output = its index number
# print(friends.index("Kevin"))

# count number of times an entry appears in list
print(friends.count("Jim"))

# sort list into alphabetical / ascending order
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

# reverse list into reverse order
# friends.reverse()

# copy a list to a new list
friends2 = friends.copy()
print(friends2)

