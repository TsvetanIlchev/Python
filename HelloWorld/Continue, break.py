shopping_list = ["milk", "eggs", "pasta", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring the " + item)
#         continue
#
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]

nasty_food_item = ''
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    print("I will have a plate of that, then, please.")

if nasty_food_item == 'spam':
    print("Can i have anything without spam in it?")
