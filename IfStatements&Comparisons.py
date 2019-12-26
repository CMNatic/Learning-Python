#compare the given inputs and print the biggest number

# >= greater than or equal too
# == two values are equal e.g. num1 == num2 (2 = 2)
# != if not equal too 
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
