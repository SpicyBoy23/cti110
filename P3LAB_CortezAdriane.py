y = int(input(""))

if (y % 400 == 0) and (y % 100 == 0):
    print("{0} - leap year".format(y))
elif (y % 4 ==0) and (y % 100 != 0):
    print("{0} - leap year".format(y))
#if not
else:
    print("{0} - not a leap year".format(y))