"""Testing Fibonacci Series"""
import pytest

FIB = [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5)]


@pytest.mark.parametrize('input, result', FIB)
def test_fibonacci(input, result):
    """Test for fibonacci."""
    from series import fibonacci
    assert fibonacci(input) == result


LUCAS = [(1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11)]


@pytest.mark.parametrize('input, result', LUCAS)
def test_lucas(input, result):
    """Test for lucas"""
    from series import lucas
    assert lucas(input) == result


SUM = [(0, 0, 1, 0), (0, 2, 1, 2), (1, 2, 1, 1), (5, 2, 1, 11), (11, 0, 1, 89)]


@pytest.mark.parametrize('a, b, c, result', SUM)
def test_sum_series(a, b, c, result):
    """Test for sum_series."""
    from series import sum_series
    assert sum_series(a, b, c) == result
