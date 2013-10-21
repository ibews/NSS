import unittest

from uebung1 import mysucc
from uebung1 import mymax

class Uebung1test(unittest.TestCase):
    def test_mysucc_positive_int_correct_result(self):
        result = mysucc(1)
        self.assertEqual(result,2)
    def test_mysucc_positive_int_correct_result2(self):
        result = mysucc(12)
        self.assertEqual(result,13)
    def test_mysucc_negative_int_correct_result(self):
        result = mysucc(-1)
        self.assertEqual(result,0)

    def test_mymax_two_ints_biggest(self):
        result = mymax(4,5)
        self.assertEqual(result, 5)
    def test_mymax_two_ints_biggest2(self):
        result = mymax(14,51)
        self.assertEqual(result, 51)
    def test_mymax_different_sign_positive(self):
        result = mymax(14,-51)
        self.assertEqual(result, 14)
