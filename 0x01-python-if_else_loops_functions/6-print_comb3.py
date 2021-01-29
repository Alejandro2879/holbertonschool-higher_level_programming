#!/usr/bin/python3


for iter in range(9):
        for i2 in range(iter + 1, 10):
                if iter == 8 and i2 == 9:
                        print('{}{}'.format(iter, i2), end="")
                else:
                        print('{}{}'.format(iter, i2), end=", ")
print()
