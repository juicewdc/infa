def f(x, y):
    if x > y or x == 16:#тут x>y пишется по дефолту, a вместо 16 пишешь число,которое надо избегать
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y)+f(x**2,y)#задаешь через f() команды которые даны в условии
print(f(3, 20) * f(20, 26))#в первой скобке от начального до того, которое "содержить", во второй скобке от содержанного до финального