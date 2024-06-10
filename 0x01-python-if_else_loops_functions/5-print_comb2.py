#!/usr/bin/python3
for k in range(0, 100):
    if k == 99:
        print(k)
    else:
        print("{:0>2d}".format(k), end=", ")
