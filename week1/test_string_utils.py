import pytest
from string_utils import *

def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_reverse_string():
    assert reverse_string("abc") == "cba"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_palindrome_true():
    assert is_palindrome("madam") == True

def test_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_word_count():
    assert word_count("hello world") == 2

def test_word_count_spaces():
    assert word_count("  hello  ") == 1

def test_capitalise():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_single():
    assert capitalise_words("hello") == "Hello"

def test_remove_duplicates():
    assert remove_duplicates("aaabbb") == "ab"

def test_remove_duplicates_long():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_none_input():
    with pytest.raises(TypeError):
        count_vowels(None)

def test_single_char():
    assert reverse_string("a") == "a"

def test_only_spaces():
    assert word_count("   ") == 0

def test_even_more():
    assert is_palindrome("racecar") == True

def test_case_sensitive():
    assert count_vowels("AEIOU") == 5

def test_duplicates_edge():
    assert remove_duplicates("aaaa") == "a"