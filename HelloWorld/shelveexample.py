import shelve

# with shelve.open("ShelveTest") as fruit:
fruit = shelve.open('ShelveTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['lemon'] = "yellow citrus fruit"
# fruit['lime'] = "sour green citrus fruit"

# print(fruit["lemon"])
# print(fruit["lime"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

fruit.close()
