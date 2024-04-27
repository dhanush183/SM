
class WordProcessor:
# method to generate count of alphabets in a string
 #  def count_alphabets(self, text):
 #       return sum(1 for char in text if char.isalpha())

# method to generate count of numbers in a string
    def count_numbers(self, text):
        return sum(1 for char in text if char.isdigit())

  #  def is_palindrome(self, text):
   #     return stripped_text == stripped_text[::-1]

  #  def replace_string(self, text, old, new):
   #     return text.replace(old, new)