import unittest
from bence import is_prime
class TestPrimeFunction(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
    def test_non_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
    def test_large_prime(self):
        self.assertTrue(is_prime(9973))
    def test_large_non_prime(self):
        self.assertFalse(is_prime(10000))
if __name__ == '__main__':
    unittest.main() 
