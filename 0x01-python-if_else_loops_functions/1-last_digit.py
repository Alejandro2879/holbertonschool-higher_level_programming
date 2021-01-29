#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l = abs(number) % 10

if number < 0:
    l *= -1

if l == 0:
    print("Last digit of {} is {} and is 0".format(number, l))

elif l > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l))

else:
    print("Last digit of {}".format(number), end=" ")
    print("is {} and is less than 6 and not 0".format(l))
