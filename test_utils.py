import pytest

from utils import expr_cleared

def test_replace():
    """ проверяем замену символов """
    expr = '''MATH.pow(3, 2) + 2 ^ 3 ?!'":;_'''
    expr = expr_cleared(expr)
    expected = 'pow(3,2)+2**3'
    assert expr == expected
