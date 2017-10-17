"""Testing Fibonacci Series"""
import pytest
import pytestwatch

def test_fib():
    from series import fibonacci
    assert fibonacci(0) == 10
