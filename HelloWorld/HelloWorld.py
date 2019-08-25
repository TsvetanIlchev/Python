age = 24
print('My age is ' + str(age) + ' years')
print('My age is {0} years'.format(age))

print("""
January:{2}
February:{0}
March:{2}
April:{1}
May:{2}
June:{1}
July:{1}
August:{2}
September:{1}
October:{1}
November:{2}
December:{2}
""".format(28, 30, 31))

print("My age is %d." % age)

for i in range(1, 12):
    print('No. %2d is %4d and cubed is %4d' % (i, i ** 2, i ** 3))
