import unittest
from app.utils import string_utils


class MyTestCase(unittest.TestCase):
    def test_concatenate(self):
        results = string_utils.concatenate('Hello', 'there')
        self.assertEqual(results, 'Hello there')

    def test_repeat(self):
        results = string_utils.repeat('a', 3)
        self.assertEqual(results, 'aaa')

    def test_repeat_2(self):
        results = string_utils.repeat('abc', 3)
        self.assertEqual(results, 'abcabcabc')

    def test_repeat_with_spacer(self):
        results = string_utils.repeat('a', 3, 'b')
        self.assertEqual(results, 'ababa')

    def test_repeat_with_spacer_2(self):
        results = string_utils.repeat('a', 3, ' ')
        self.assertEquals(results, 'a a a')


if __name__ == '__main__':
    unittest.main()
