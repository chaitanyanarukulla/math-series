"""Testing Fibonacci Series"""
import pytest
#import pytestwatch

def test_fib(n):
    from series import fibonacci
    assert fibonacci(n) == 10


def test_fib2():
    from series import fibonacci
    assert fibonacci(n) == 0
