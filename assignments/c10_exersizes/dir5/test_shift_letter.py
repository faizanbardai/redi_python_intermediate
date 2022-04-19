"""
Implement the following specifications / test functions for the function shift_letter:

- test_shift_letter_increments_beginning_letters(). Examples:
    - shift_letter("a",1) produces "b"
    - shift_letter("a",3) produces "d"
- test_shift_letter_wraps_around_alphabet(). Examples
    - shift_letter("z",1) produces "a"
    - shift_letter("x",4) produces "b"
- test_shift_letter_keeps_letter_capitalization(). Examples:
    - shift_letter("a",1) produces "b"
    - shift_letter("A",1) produces "B"
- test_shift_letter_works_with_negative_steps(). Examples:
    - shift_letter("g",-1) produces "f"
    - shift_letter("g",-6) produces "a"
- test_shift_letter_yields_identity_for_some_steps(). Examples:
    - shift_letter(<LETTER>, 0) produces <LETTER> for all 26 letters (a-z)
    - shift_letter(<LETTER>, 26) produces <LETTER> for all 26 letter (a-z)
    - shift_letter(<LETTER>, 52) produces <LETTER> for all 26 letter (a-z)

When you run the test, they will be automatically run against four implementations of "shift_letter":
- shift_letter_correct
- shift_letter_wrong1
- shift_letter_wrong2
- shift_letter_wrong3

For each function, write down which tests it passes and which test it fails.

1. test_shift_letter_increments_beginning_letters
    - shift_letter_correct  [pass]
    - shift_letter_wrong1   [pass]
    - shift_letter_wrong2   [pass]
    - shift_letter_wrong3   [pass]
2. test_shift_letter_works_with_negative_steps
    - shift_letter_correct  [pass]
    - shift_letter_wrong1   [pass]
    - shift_letter_wrong2   [pass]
    - shift_letter_wrong3   [fail]
3. test_shift_letter_wraps_around_alphabet
    - shift_letter_correct  [pass]
    - shift_letter_wrong1   [pass]
    - shift_letter_wrong2   [pass]
    - shift_letter_wrong3   [pass]
4. test_shift_letter_keeps_letter_capitalization
    - shift_letter_correct  [pass]
    - shift_letter_wrong1   [fail]
    - shift_letter_wrong2   [fail]
    - shift_letter_wrong3   [pass]
5. test_shift_letter_yields_identity_for_some_steps
    - shift_letter_correct  [pass]
    - shift_letter_wrong1   [fail]
    - shift_letter_wrong2   [pass]
    - shift_letter_wrong3   [pass]

"""
from .shift_letter import (
    shift_letter_correct,
    shift_letter_wrong1,
    shift_letter_wrong2,
    shift_letter_wrong3,
)
import pytest


@pytest.fixture(
    params=[
        shift_letter_correct,
        shift_letter_wrong1,
        shift_letter_wrong2,
        shift_letter_wrong3,
    ]
)
def shift_letter(request):
    # Don't modify this function!
    # This function is needed to iterate over all implementations of "shift_letter".
    # You also don't need to understand it, it's rather advanced pytest stuff.
    return request.param


def test_shift_letter_increments_beginning_letters(shift_letter):
    # This is already done for you ;).
    assert shift_letter("a", 1) == "b"
    assert shift_letter("a", 3) == "d"


def test_shift_letter_wraps_around_alphabet(shift_letter):
    assert shift_letter("z", 1) == "a"
    assert shift_letter("x", 4) == "b"
    ...


def test_shift_letter_keeps_letter_capitalization(shift_letter):
    assert shift_letter("a", 1) == "b"
    assert shift_letter("A", 1) == "B"
    ...


def test_shift_letter_works_with_negative_steps(shift_letter):
    assert shift_letter("g", -1) == "f"
    assert shift_letter("g", -6) == "a"
    ...


def test_shift_letter_yields_identity_for_some_steps(shift_letter):
    assert shift_letter("a", 0) == "a"
    assert shift_letter("a", 26) == "a"
    assert shift_letter("a", 52) == "a"
    ...
