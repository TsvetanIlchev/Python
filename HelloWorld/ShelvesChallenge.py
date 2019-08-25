# import shelve
#
# books = shelve.open("book")
# books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
#                     "beans_on_toast": ["beans", "bread"],
#                     "scrambled_eggs": ["eggs", "butter", "milk"],
#                     "soup": ["tin of soup"],
#                     "pasta": ["pasta", "cheese"]}
# books["maintenance"] = {"stuck": ["oil"],
#                        "loose": ["gaffer tape"]}
#
# print(books["recipes"])
# # print(books["recipes"]["scrambled_eggs"])
# #
# # print(books["maintenance"]["loose"])
#
# books.close()

# Modify the program from the Second Dictionary challenge of lecture 56
# to use shelves instead of dictionaries.
#
# Do this by creating two programs. cave_initialise.py should create the two
# shelves (locations and vocabulary) with the appropriate keys and values.
#
# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 45, everything
# before that (modified to use shelves) will be in cave_initialise.py.
