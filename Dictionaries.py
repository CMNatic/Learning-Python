# store data in key value pairs, and refere to it by its key in the dictionary

# think of a normal dictionary: the word = the key, the definition = the value

# convert 3 digit month to full length
# Jan -> January

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

#get means the possibility of putting in a key that doesn't have a value
print(monthConversions.get("December", "Not a valid key"))