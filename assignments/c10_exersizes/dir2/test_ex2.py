import pytest
from .ex2 import number_guessing_game


def test_game_prints_congratulation_on_first_try(monkeypatch, capsys):
    for number in [1, 3]:
        _patch_input_and_randint(monkeypatch, fake_input=[number] * 3)
        number_guessing_game()
        assert "congrat" in capsys.readouterr().out.lower()


def test_game_prints_congratulation_on_later_try(monkeypatch, capsys):
    _patch_input_and_randint(
        monkeypatch, fake_input=[0, 10, 1, 2, 5, 7], random_integer=7
    )
    number_guessing_game()
    assert "congrat" in capsys.readouterr().out.lower()


def test_game_prints_bigger_if_guess_too_big(monkeypatch, capsys):
    _patch_input_and_randint(monkeypatch, fake_input=[0, 10, 7, 5], random_integer=5)
    number_guessing_game()
    assert "bigger" in capsys.readouterr().out.lower()


def test_game_prints_smaller_if_guess_too_small(monkeypatch, capsys):
    _patch_input_and_randint(monkeypatch, fake_input=[0, 10, 3, 5], random_integer=5)
    number_guessing_game()
    assert "smaller" in capsys.readouterr().out.lower()


def _patch_input_and_randint(_monkeypatch, fake_input, random_integer=None):
    _patch_input(_monkeypatch, fake_input)
    if random_integer is not None:
        _patch_randint(_monkeypatch, random_integer)


def _patch_input(_monkeypatch, fake_input: list):
    fake_input = iter(fake_input)

    def my_input(text=None) -> str:
        return str(next(fake_input))

    _monkeypatch.setattr("builtins.input", my_input)


def _patch_randint(_monkeypatch, random_int):
    class MyRandomNumber:
        def __init__(self, random_int: int):
            self.call_count = 0
            self.random_int = random_int

        def __call__(self, a, b):
            self.call_count += 1
            if self.call_count > 1:
                raise ValueError(
                    "randint was called more than once, this is not correct!"
                )
            return self.random_int

    _monkeypatch.setattr("random.randint", MyRandomNumber(random_int).__call__)
