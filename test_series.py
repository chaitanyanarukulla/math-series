"""Testing Fibonacci Series"""
import pytest
#import pytestwatch

def test_fib():
    from series import fibonacci
    assert fibonacci(0) == 0


def test_fib2():
	from series import fibonacci
	assert fibonacci(0) == 0


def test_lucas():
	from series import lucas
	assert lucas(2) == 2


def test_lucas2():
	from series import lucas
	assert lucas(1) == 3