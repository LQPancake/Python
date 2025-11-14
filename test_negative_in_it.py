import unittest
from negative_in_it import isNegative
class TestNegative(unittest.TestCase):
    def test_negative_number(self):
        self.assertTrue(isNegative([9, 12, 3, -7, 53]))
        self.assertTrue(isNegative([-9, -12, -3, 7, -53]))
        self.assertTrue(isNegative([-9, -12, 3, -7, 53]))
        self.assertTrue(isNegative([9, 12, -3, -7, -53]))
    def test_not_is_negative(self):
        self.assertFalse(isNegative([15, 1, 124, 9, 0, 14]))
        self.assertFalse(isNegative([15]))
        self.assertFalse(isNegative([]))
        self.assertFalse(isNegative([0, 231212331, 12, 78]))
if __name__ == '__main__':
    unittest.main()