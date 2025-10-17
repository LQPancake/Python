import unittest
from validation import validation
class TestValidation(unittest.TestCase):
    def test_too_small_value(self):
        self.assertEqual(validation(-3), False)
        self.assertEqual(validation(0), False)
    def test_correct_value(self):
        self.assertEqual(validation(1), True)
        self.assertEqual(validation(4), True)
        self.assertEqual(validation(5), True)
    def test_too_big_value(self):
        self.assertEqual(validation(6), False)
        self.assertEqual(validation(9), False)
if __name__ == '__main__':
    unittest.main()
