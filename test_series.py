"""Testing Fibonacci Series"""
import pytest
#import pytestwatch

def test_fib(n):
    from series import fibonacci
    assert fibonacci(n) == 10
