"""This is function exercise based on the fibonacci sequence."""

def fibonacci(n):
#this function  outputs  fibonacci number of nth value
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
#this function  outputs lucas number of nth value
    if n == 2:
        return 2
    if n == 1:
        return 3
    return lucas(n - 1) + lucas(n - 2)

def  sum_series(n, a = 0, b = 1):
    
    if a == 2 and b == 1:
        return lucas(n)
    # elif a != 2 and b != 1:
    #     return fibonacci(n - a ) + fibonacci(n - b)
    else:
        return fibonacci(n)