import unittest
from simple_calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 10), 20)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multilpication(self):
        self.assertEqual(self.calc.multiply(5, 10), 50)

    def text_division(self):
        self.assertEqual(self.calc.divide(20, 10), 2)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

