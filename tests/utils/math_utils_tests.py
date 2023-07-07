import unittest
from app.utils import math_utils


class MyTestCase(unittest.TestCase):
    def test_add(self):
        results = math_utils.add(1, 4)
        self.assertEqual(results, 5)

    def test_subtract(self):
        results = math_utils.subtract(4, 1)
        self.assertEqual(results, 3)

if __name__ == '__main__':
    unittest.main()
