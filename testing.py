#!/usr/bin/env python

nList = open("numberList.txt", "w+")
n = 00000000

while n < 100000000:
        if n % 10000 == 0:
                print("Completed", n, "number of lines so far!")
        nStr = str(n)
        nList.write(nStr)
        nList.write("\n")
        n += 1
nList.close()
print("Done!")
