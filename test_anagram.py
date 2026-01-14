import unittest

from anagram import are_anagrams

class TestAnagramDetector(unittest.TestCase):
    def test_simple_anagrams(self):
        self.assertTrue(are_anagrams("listen","silent"))

    def test_not_anagrams(self):
        self.assertFalse(are_anagrams("hello","world"))

if __name__ == "__main__":
    unittest.main()