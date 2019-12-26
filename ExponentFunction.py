
def raise_to_power(base_num, power_num):
    result = 1
    # loop through for loop as many times as there is "power_num"
    for index in range(power_num):
        result = result * base_num # result = base number * how ever many power_number there is
    return result

print(raise_to_power(3, 4))