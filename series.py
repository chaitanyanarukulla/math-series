"""This function exercise is based on the fibonacci sequence."""


def fibonacci(n):
    """This function outputs fibonacci number of nth value."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """This function outputs lucas number of nth value."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """This function outputs the sum of series."""
    if n == 0:
        return a
    if n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)

if __name__ == "__main__":
    print(__doc__)
    print(fibonacci())
    print(fibonacci.__doc__)
    print(lucas())
    print(lucas.__doc__)
    print(sum_series())
    print(sum_series.__doc__)
