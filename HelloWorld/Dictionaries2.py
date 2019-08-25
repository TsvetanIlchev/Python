locations = {0: "You are sitting in front of your computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of the hill",
             3: "You are inside of a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exist = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W"}

loc = 1
while True:
    availableExits = ", ".join(exist[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExits + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exist[loc]:
        loc = exist[loc][direction]
    else:
        print("You cannot go in that direction")
