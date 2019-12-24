# can be used to put some related values into a list to be easily retrieved for later use.
# you can put strings, numbers, booleans into lists

# friends = ["Kevin", 2, True]

friends = ["Kevin", "Karen", "Jim"]

# we can print out specifics from list using their index

# friends = ["Kevin", "Karen", "Jim"]
#               0        1       2

print(friends[1])

# selecting multiple entries from list
print(friends[1:])

# modify value "Karen" to "Mike"
friends[1] = "Mike"
print(friends[1])
