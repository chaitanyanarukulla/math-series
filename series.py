"""This function exercise is based on the fibonacci sequence."""

def fibonacci(n):
    """this function outputs fibonacci number of nth value"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """this function outputs lucas number of nth value"""
    if n == 2:
        return 2
    if n == 1:
        return 3
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a = 0, b = 1):
    """this function outputs the sum of series"""
    if n == 0:
        return a
    if n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)

if __name__ == "__main__":
    print(__doc__)
    print(fibonacci(3))
    print(fibonacci.__doc__)
    print(lucas(3))
    print(lucas.__doc__)
    print(sum_series(3,4,2))
    print(sum_series.__doc__)