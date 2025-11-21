import unittest
from kerulet import kerulet;
class TestPerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(kerulet(8), 32)
        self.assertEqual(kerulet(8, 6), 28)
        self.assertEqual(kerulet(8, 6, 5), 19)
        self.assertEqual(kerulet(8, 6, 5, 9), 28)
        self.assertEqual(kerulet(8, 6, 5, 9, 4), 32)
if __name__ == '__main__':
    unittest.main()