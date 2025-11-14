import unittest
from shop import is_open

class TestIsOpen(unittest.TestCase):
    def test_open_hours(self):
        self.assertTrue(is_open(8))
        self.assertTrue(is_open(10))
        self.assertTrue(is_open(15))

    def test_closed_hours(self):
        self.assertFalse(is_open(7))
        self.assertFalse(is_open(16))
        self.assertFalse(is_open(20))

if __name__ == 'main':
    unittest.main()