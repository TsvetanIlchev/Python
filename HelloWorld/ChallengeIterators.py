my_items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_days = ["Monday", "Tuesday", "Wednesday"]

my_iterator = iter(my_items)
my_days_iter = iter(my_days)

for item in range(len(my_days)):
    print(next(my_days_iter))