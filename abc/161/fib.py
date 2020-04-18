def fib(n):
    if n == 0 or 1:
        return n
    else:
        return fib(n-1) + fib(n-2)