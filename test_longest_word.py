import pytest
from longest_word import longest_word

def test_longest_word():
    assert longest_word("The quick brown fox jumps over the lazy dog") == 'jumps'

def test_longest_word_empty():
    assert longest_word("") == ''

def test_longest_word_single_word():
    assert longest_word("Hello") == 'Hello'


if __name__ == "__main__":
    pytest.main()