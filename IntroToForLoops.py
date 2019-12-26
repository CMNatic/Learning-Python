# allows to loop over different collections of items
# loop over different arrays, or loop through series of numbers etc

# example 1
# for every letter in "Giraffe" do...
i = 0
word = "giraffe"
for letter in word:
    print(letter)
    i += 1
print("There are " + str(i) + " numbers in " + word)

# examples 2 and 3
friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

# give a range between 0 and the number of friends in "friends" len is length
for index in range(len(friends)):
    print(index)