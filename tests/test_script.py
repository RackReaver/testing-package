import pytest


import script

def test_add():
    assert script.add(2, 2) == 4
    assert script.add(2, 3) == 5
    assert script.add(0, 1) == 1
    assert script.add(5, 10) == 15

def test_subtract():
    assert script.subtract(2, 2) == 0
    assert script.subtract(6, 2) == 4
    assert script.subtract(1, 2) == -1
    assert script.subtract(-1, 2) == -3