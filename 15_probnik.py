b=[]
def f(x):
    return (x & a == 0) or (not(x & 37 == 0) or (not(x&12==0)))

for a in range(1,100000):
    if all(f(x) for x in range(1,100000)):
        b.append(a)
        print(max(b))