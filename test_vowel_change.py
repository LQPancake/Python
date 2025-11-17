import unittest
from vowel_change import change_vowels

class TestVowelChange(unittest.TestCase):
    def test_vowel_change(self):
        self.assertEqual(change_vowels("alma"), ".lm.")
        self.assertEqual(change_vowels("körte"), "k.rt.")
        self.assertEqual(change_vowels("tükörfúrógép"), "t.k.rf.r.g.p")
        self.assertEqual(change_vowels("farok"), "f.r.k")
        self.assertEqual(change_vowels("SZKTV"), "SZKTV")
if __name__ == '__main__':
    unittest.main()