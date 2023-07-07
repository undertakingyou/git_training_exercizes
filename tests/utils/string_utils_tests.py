import unittest
from app.utils import string_utils


class MyTestCase(unittest.TestCase):
    def test_concatenate(self):
        results = string_utils.concatenate('Hello', 'world')
        self.assertEqual(results, 'Hello world')
