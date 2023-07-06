import unittest
from app.utils import string_utils


class MyTestCase(unittest.TestCase):
    def test_concatenate(self):
        results = string_utils.concatenate("Hello", "there")
        self.assertEqual(results, "Hello there")  # add assertion here


if __name__ == '__main__':
    unittest.main()
