"""Contains Tests for different Calc Functions"""
from cal import add, div, mul, sub
def test_add():
    """test addition functionality"""
    assert add(2,2)==4

def test_sub():
    """test subtraction functionality"""
    assert sub(7,5)==2

def test_mul():
    """test multiplication functionality"""
    assert mul(7,5)==35

def test_div():
    """test division functionality"""
    assert div(4,2)==2
