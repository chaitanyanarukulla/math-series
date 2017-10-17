"""This is function exercise based on the fibonacci sequence."""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 2:
        return 2
    if n == 1:
        return 3
    return lucas(n - 1) + lucas(n - 2)