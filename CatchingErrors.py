
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero" + err)
except:
    print("Invalid input")