import unittest
from word_processor import WordProcessor

#Integration testing for all test cases
class Integration(unittest.TestCase):
    def test(self):
        text = '12madam21'
        self.assertEqual(WordProcessor.count_numbers(self, text), 4)
        self.assertEqual(WordProcessor.count_alphabets(self, text), 5)
        self.assertEqual(WordProcessor.is_palindrome(self, text), True)
        self.assertEqual(WordProcessor.replace_string(self, text, 'a', 's'), '12msdsm21')


if __name__ == "__main__":
    unittest.main()
