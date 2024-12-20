from fnmatch import *
from sys import setrecursionlimit
setrecursionlimit(10000)
for x in range(98591,10**12+1,98591):
    s=str(x)
    if fnmatch(str(x),"12?3*456??9"):
        if x%98591==0:
            print(x,x//98591)