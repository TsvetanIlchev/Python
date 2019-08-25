fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making a sider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet, fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])

print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break

    # description = fruit.get(dict_key, "There is no " + dict_key + " in dictionary.")
    # print(description)


    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("There is no such " + dict_key + " in dictionary.")

# for snack in fruit:
#     print(fruit[snack])

for f in sorted(list(fruit.keys())):
    print()

