import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate('5 3 *')
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate('6 3 /')
        self.assertEqual(2, result)
    
    # extension
    def test_decimal(self):
        result = rpn.calculate('2.3 6 +')
        self.assertEqual(8.3, result)
    def test_percent(self):
        result = rpn.calculate('20 25 % +')
        self.assertEqual(25, result)
    def test_exponent(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
    def test_intdiv(self):
        result = rpn.calculate('5 2 //')
        self.asvsertEqual(2, result)
    def test_factorial(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)
    def test_bitAnd(self):
        result = rpn.calculate('3 1 &')
        self.assertEqual(1, result)
    def test_bitOr(self):
        result = rpn.calculate('3 1 |')
        self.assertEqual(3, result)
    def test_bitNot(self):
        result = rpn.calculate('3 ~')
        self.assertEqual(-4, result)
