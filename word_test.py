import unittest
from word_processor import WordProcessor


class TestWordProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = WordProcessor()

    def test_count_alphabets(self):
        self.assertEqual(self.processor.count_alphabets("Hello World 123"), 10)

    def test_count_numbers(self):
        self.assertEqual(self.processor.count_numbers("Hello World 123"), 3)

    def test_is_palindrome(self):
        self.assertTrue(self.processor.is_palindrome("mam"))

    def test_replace_string(self):
        self.assertEqual(self.processor.replace_string("Hello World 123", "H", "W"), "Wello World 123")


if __name__ == '__main__':
    unittest.main()
