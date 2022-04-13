from .ex1 import (
    first_item_equals_last_item,
    get_even_indexed_chars,
    remove_chars,
    one_in_common,
    is_palindrome_number,
)


def test_first_item_equals_last_item():
    assert first_item_equals_last_item([1, 2, 3, 1]) == True
    assert first_item_equals_last_item([1]) == True
    assert first_item_equals_last_item([None, "abc", None]) == True

    assert first_item_equals_last_item([None, "abc", 1]) == False
    assert first_item_equals_last_item([2, "a"]) == False


def test_get_even_indexed_chars():
    assert get_even_indexed_chars("abc") == "ac"
    assert get_even_indexed_chars("hello world") == "hlowrd"


def test_remove_chars():
    assert remove_chars("python", 2) == "thon"
    assert remove_chars("hello", 2) == "llo"
    assert remove_chars("ab", 2) == ""


def test_one_in_common():
    assert one_in_common({1, 2, 3}, {2}) == True
    assert one_in_common({1, 2, 3}, {1}) == True
    assert one_in_common({"a", "b"}, {1}) == False
    assert one_in_common({"a", "b"}, {}) == False


def test_is_palindrome_number():
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(454) == True
    assert is_palindrome_number(4) == True
    assert is_palindrome_number(456) == False
    assert is_palindrome_number(45) == False
