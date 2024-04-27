from word_processor import WordProcessor

word_processor = WordProcessor()


def test_count_alphabets():
    text = "Hello World 123"
    exp_result = 10
    result = word_processor.count_alphabets(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"


def test_count_numbers():
    text = "Hello World 123"
    exp_result = 3
    result = word_processor.count_numbers(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"


def test_is_palindrome():
    text = "Hello World 123"
    exp_result = False
    result = word_processor.is_palindrome(text)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"


def test_replace_string():
    text = "Hello World 123"
    old_str = 'H'
    new_str = 'W'
    exp_result = "Wello World 123"
    result = word_processor.replace_string(text, old_str, new_str)
    assert result == exp_result, f"Expected: {exp_result}, but got: {result}"

