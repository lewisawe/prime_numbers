import unittest
from primeNumber import *
class primeNumber(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_no_input(self):
        self.assertIsNone(is_prime(None))

    def test_is_integer(self):
        self.assertIsInstance(is_prime(5, int))

    def test_primein_0_to_negativeInt(self):
        with self.assertRaises(TypeError):
            is_prime(-20)

    def test_NonInteger_input(self):
        with self.assertRaises(TypeError):
            is_prime([])

if __name__ == '__main__':
    
