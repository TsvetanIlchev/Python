age = int(input("How old are you?"))

if not(age < 18):
    print("You are old enough to vore.")
    print("Please put X in the box.")
else:
    print("Please come back after {} years". format(18 - age))