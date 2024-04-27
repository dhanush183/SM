import unittest
from word_processor import WordProcessor

#Integration testing for all test cases
class Integration(unittest.TestCase):
    def test(self):
        text = '12madam21'
        self.assertEqual(WordProcessor.count_numbers(self, text), 4) #test for numbers count
        self.assertEqual(WordProcessor.count_alphabets(self, text), 5) #test for alphabets count
        self.assertEqual(WordProcessor.is_palindrome(self, text), True) #test for checking palindrome or not
        self.assertEqual(WordProcessor.replace_string(self, text, 'a', 's'), '12msdsm21') #test for replace the string


if __name__ == "__main__":
    unittest.main()
