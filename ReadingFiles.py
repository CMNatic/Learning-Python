
# r = read
# w = write
# a = append info, can only add to file
# r+ = read & write
employee_file = open("employees.txt", "r")

# find out if the file is only readable
print(employee_file.readable())

# find out if the file is writeable
print(employee_file.writable())

# read & output whole file
print(employee_file.read())

# read first line of the file
print(employee_file.readline())

# read multiple lines of file, it'll put them into a list
print(employee_file.readlines())

# read a specific line
print(employee_file.readlines()[1])


# example of a for loop
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
# always make sure you close the file after use