age = int(input("How old are you?"))

# if  (age >= 16 and age <= 65):
#     print("Have a good day at work.")
# if 15 < age < 66:
#     print("Have a good day at work.")

if (age < 16) or (age > 65):
    print("Enjoy your life.")
else:
    print("Have a good day at work.")
