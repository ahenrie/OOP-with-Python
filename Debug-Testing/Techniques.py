# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

if __name__ == '__main__':
    unittest.main()

######################################################
#Pytest

# test_calculator_pytest.py
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

#####################################################
#Doctest
# calculator_doctest.py
class Calculator:
    def add(self, a, b):
        """
        Add two numbers.
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.add(-1, 1)
        0
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.
        >>> calc = Calculator()
        >>> calc.subtract(5, 3)
        2
        >>> calc.subtract(3, 5)
        -2
        """
        return a - b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

