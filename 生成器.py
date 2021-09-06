"""
斐波那契数列
"""


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        n += 1
        yield a
        a, b = b, a + b


fib = fib(10)

while True:
    try:
        y = next(fib)
        print(y, end=' ')
    except Exception as e:
        print(e)
        break
