import unittest
from main import calc

class TestY(unittest.TestCase):
    def test_area(self):
        self.assertEqual(calc('1, 2, 3'), '3.0, 10.0, 21.0')

