#!/usr/bin/python3
def fizzbuzz():
    for iter in range(1, 101):
        if (iter % 3) == 0 and (iter % 5) == 0:
            print("FizzBuzz ", end="")
        elif (iter % 3) == 0:
            print("Fizz ", end="")
        elif (iter % 5) == 0:
            print("Buzz ", end="")
        else:
            print('{} '.format(iter), end="")
