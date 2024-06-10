#!/usr/bin/python3
for k in range(0, 9):
    for j in range(k + 1, 10):
        if k == 8:
            print("{}{}".format(k, j))
        else:
            print("{}{}".format(k, j), end=", ")
