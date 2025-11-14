import unittest
from longerWord import get_longer_word
class testLongerWord(unittest.TestCase):
    def test_FirstShort(self):
        self.assertEqual(get_longer_word("iskola", "ház"), "iskola")
        self.assertEqual(get_longer_word("viziló", "egér"), "viziló")
    def test_FirstLong(self):
        self.assertEqual(get_longer_word("iskola", "edzőterem"), "edzőterem")
        self.assertEqual(get_longer_word("viziló", "elefánt"), "elefánt")
    def test_Equal(self):
        self.assertEqual(get_longer_word("iskola", "otthon"), "egyforma")
        self.assertEqual(get_longer_word("viziló", "tigris"), "egyforma")
if __name__ == '__main__':
    unittest.main()