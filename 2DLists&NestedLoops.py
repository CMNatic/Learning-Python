
#
number_grid = [
    #0 #1 #2
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9], #2
    [0]  # 4 rows, 3 columns
]

# to access individual value in this list
# print(number_grid[0][0])

# to print all the values in the list
# nested for loop is a for loop in a for loop
for row in number_grid:
    for col in row:
        print(col)