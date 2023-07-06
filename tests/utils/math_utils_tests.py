import unittest
from app.utils import math_utils

class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = math_utils.add(2, 2)
        self.assertEqual(result, 4)

    def test_subtract(self):
        result = math_utils.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = math_utils.multiply(3, 1)
        self.assertEqual(result, 3)

    def test_divide(self):
        result = math_utils.divide(8, 2)
        self.assertEqual(result, 4)

    def test_double(self):
        result = math_utils.double(6)
        self.assertEqual(result, 12)

    def test_square(self):
        result = math_utils.square(3)
        self.assertEqual(result, 9)

    def test_square_root(self):
        result = math_utils.square_root(16)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
