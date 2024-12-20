from sys import setrecursionlimit
setrecursionlimit(10000)#Это чтобы программа заработала так как чисел многа
def f(n):
    if n<=3:
        return 1#F(n)=1 при n<=3
    if n>3:
        return (n+3)*f(n-2)#F(n)=(n+3)*F(n-2) если n>3
#По сути просто переписывешь условие на языке пайтон
a=f(2028)/f(2024)#находишь значение выражения
print(a)#Выводишь его