"""Testing Fibonacci Series"""
import pytest

FIB = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (11, 89), (12, 144), (20, 6765)]


@pytest.mark.parametrize('input, result', FIB)
def test_fibonacci(input, result):
    """Test for fibonacci."""
    from series import fibonacci
    assert fibonacci(input) == result


LUCAS = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18)]


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
