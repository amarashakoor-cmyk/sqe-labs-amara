def count_vowels(text):
    if text is None:
        raise TypeError
    return sum(1 for c in text.lower() if c in "aeiou")

def reverse_string(text):
    if text is None:
        raise TypeError
    return text[::-1]

def is_palindrome(text):
    if text is None:
        raise TypeError
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def word_count(text):
    if text is None:
        raise TypeError
    return len(text.split())

def capitalise_words(text):
    if text is None:
        raise TypeError
    return text.title()

def remove_duplicates(text):
    if text is None:
        raise TypeError
    result = ""
    for c in text:
        if not result or result[-1] != c:
            result += c
    return result