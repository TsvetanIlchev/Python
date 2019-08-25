# my_list = list(range(10))
#
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))

decimals = range(0, 100)
my_range = decimals[3:40:3]

print(my_range == range(3, 40, 3))

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)
