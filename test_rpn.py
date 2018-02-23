import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)

    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)

    def test_subtracts(self):
        result = rpn.calculate('5 2 - 2 -')
        self.assertEqual(1, result)

    def test_addAndSubtract(self):
        result = rpn.calculate('1 1 + 2 + 3 - 2 + 4 -')
        self.assertEqual(-1, result)

    def test_multiply(self):
        result = rpn.calculate('3 5 *')
        self.assertEqual(15, result)

    def test_multiplys(self):
        result = rpn.calculate('3 5 * 2 *')
        self.assertEqual(30, result)

    def test_divide(self):
        result = rpn.calculate('3 5 /')
        self.assertEqual((3/5), result)

    def test_divides(self):
        result = rpn.calculate('5 10 / 2 /')
        self.assertEqual(1/4, result)

    def test_all(self):
        result = rpn.calculate('5 5 + 2 - 10 + 3 - 2 * 3 /')
        self.assertEqual(10, result)

    def test_tooMany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
