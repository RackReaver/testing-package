"""
This contains a collection of test functions for learning
Git, GitHub, Travis, PyPi and more.
"""
from _version import get_versions
__version__ = get_versions()['version']
del get_versions


def add(num1, num2):
    """Adds two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers"""
    return num1 / num2
