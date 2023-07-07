import unittest
from app.utils import string_utils


class MyTestCase(unittest.TestCase):
    def test_concatenate(self):
        results = string_utils.concatenate('Hello', 'world')
        self.assertEqual(results, 'Hello world')

    def test_repeat(self):
        results = string_utils.repeat('a', 3)
        self.assertEqual(results, 'aaa')


if __name__ == '__main__':
    unittest.main()
