# used to execute code depending upon true/false conditions
# e.g. if 1+1 = 2 then do abc, if not then do xyz

is_male = False
is_tall = False

# if they are either male OR are tall, then: requires one or both values to be truth
# if is_male or is_tall:
#    print("You are either male, tall or both")
# else:
#    print("You are neither male nor tall")

# both conditions must be true with AND
if is_male and is_tall:
    print("You are a Male and Tall")

# else if e.g. Check if they are a male but aren't tall
elif is_male and not(is_tall):
    print("You are a Male, but you are not tall")

# check if they are a male or not, but are tall
elif not(is_male) and is_tall:
    print("You are not a Male, but you are tall")

else:
    print("You are neither male nor tall")