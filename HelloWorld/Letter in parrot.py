letter = input("Enter a character: ")
parrot = "Norwegian Blue"

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter.")