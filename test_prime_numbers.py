import unittest
from primeNumber import *
class primeNumber(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(8))
        self.assertFalse(is_prime(7))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(67))
        self.assertFalse(is_prime(99))
        self.assertTrue(is_prime(100))
        self.assertTrue(is_prime(54))
        self.assertTrue(is_prime(1))
        self.assertTrue(is_prime(47))
if __name__ == '__main__':
    
