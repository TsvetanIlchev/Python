range_number = range(0, 13)
b = 2

with open("imelda3.txt", 'a') as file:
    for number in range_number:
        result = number * b
        print("{0} times {1} is {2}".format(number, b, result) ,file=file)