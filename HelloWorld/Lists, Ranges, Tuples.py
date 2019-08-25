# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# items_List = ["Completed", "Reopened", "Open", "Closed", "In progress", "To be discussed"]
#
# for state in items_List:
#     print("The current state is {}".format(state))
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = odd + even
# numbers_in_order = sorted(numbers)
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("Lists are equal.")
# else:
#     print("Lists are not equal.")

#
# list_1 = []
# list_2 = list()
#
# print(list("The lists are equal."))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for numbers_set in numbers:
    print(numbers_set)

    for value in numbers_set:
        print(value)