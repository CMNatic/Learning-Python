
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Python will always convert user input into a string, so we have to make it a number
# e.g. result = num1 + num2 will combine both inputted numbers together rather then adding
# int(num1) will only accept whole decimals
# so we need to use float(num1)
result = float(num1) + float(num2)

print(result)
