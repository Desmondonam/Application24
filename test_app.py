import pytest 
from app import add

def test_add_positive_numbers():
    assert add(2,5) == 7

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_add_positive_and_negative_numbers():
    assert add(2, -3) == -1

def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0