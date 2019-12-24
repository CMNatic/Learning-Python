#

print("This is a string!")

print("\n")

print("This is a string \n with a new line!")

print("\n")

# Escape character - the following character should be taken literally (e.g. print out a quotation)

print ("This is a string\" with a quotation mark")

print("\n")

phrase = "Learning Python"

print(phrase)
print("\n")

# Concattenating is merging two strings together
print(phrase + " is cool")
print("\n")

# Function with a string e.g. converting all text to lowercase
print(phrase.lower())
print("\n")

# Convert string to uppercase
print(phrase.upper())
print("\n")

# Print length of phrase
print(len(phrase))
print("\n")

# Retrieve certain characters of string (using index) where first character is index 0 for "L"
#       L E A R N I N G   P Y T H O N
#       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
print(phrase[0])
print("\n")
# Find out where a specific character is located in a string (rather then finding it ourselves)
# this is called "parsing a paremeter" (passing a value to a function, the value is the parameter)
print(phrase.index("n"))
print("\n")

# replace characters in a string, you put what you want to change, and then the new value to change it to.
print(phrase.replace("Learning", "Python"))
print("\n")