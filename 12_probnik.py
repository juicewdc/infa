from sys import setrecursionlimit
setrecursionlimit(10000000)
def sum_dig(string):
    sm=0
    for x in string :
        sm+=int(x)
    return sm
a=[]
for n in range(4,10000):
    s='3'+'5'*n
    while '333' in s or '555' in s:
        if '555' in s:
            s.replace('555','3')
        else:
            s.replace('333','5')
    a.append(sum_dig(s))
print(max(a))