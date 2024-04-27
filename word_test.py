from word_processor import WordProcessor

word_processor = WordProcessor()

"""
def test_count_alphabets():
    text = "Hello World 123" #This line is the input text for count_alphabets testing
    exp_result = 10 # This line is for expected result
    result = word_processor.count_alphabets(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"
    
def test_count_numbers():
    text = "Hello World 123"# This line is the input text for count numbers testing
    exp_result = 3# this line is for expected output
    result = word_processor.count_numbers(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"
"""

def test_is_palindrome():
    text = "Hello World 123"#input text for this test
    exp_result = True#expected output for this test
    result = word_processor.is_palindrome(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"

"""
def test_replace_string():
    text = "Hello World 123"
    old_str = 'H'
    new_str = 'W'
    exp_result = "Wello World 123"
    result = word_processor.replace_string(text, old_str, new_str)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"
"""
