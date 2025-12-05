# USDből forintba átváltás
# teszt
import unittest
from arfolyam import usd_to_huf
class TestUsdToHuf(unittest.TestCase):
    def test_NormalRates(self):
        self.assertEqual(usd_to_huf(1, 400), 400)
        self.assertEqual(usd_to_huf(2.5, 360), 900)
    def test_ZeroOrNegative(self):
        self.assertEqual(usd_to_huf(0, 360), 0)
        self.assertEqual(usd_to_huf(-1, 360), "hibás")
    def test_DifferentRates(self):
        self.assertEqual(usd_to_huf(10, 300), 3000)
        self.assertEqual(usd_to_huf(3, 500), 1500)
if __name__ == '__main__':
    unittest.main()
