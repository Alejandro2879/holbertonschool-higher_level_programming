#!/usr/bin/python3

counter = 0
for iter in sys.argv[1:]:
    counter += 1
print('{}: arguments'.format(counter))
counter2 = 0
for iter2 in sys.argv[1:]:
    counter2 += 1
    print('{}: {}'.format(counter2, iter2))

if __name__ == "__main__":
    import sys
