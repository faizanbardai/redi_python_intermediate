from pathlib import Path
from .ex3 import caesar_encrypt, decypher_file


def test_caesar_encrypt_wraps_around_correctly():
    s1 = "hello world"
    s2 = ")(/)$(/**"
    s3 = ""
    assert caesar_encrypt(s1, 26) == s1
    assert caesar_encrypt(s2, 26) == s2
    assert caesar_encrypt(s3, 26) == s3


def test_caesar_encrypt_inverse_step_cancels_out():
    s1 = "hello world"
    s2 = "9283)(/&$§$&§"
    s3 = ""
    assert caesar_encrypt(caesar_encrypt(s1, 9), -9) == s1
    assert caesar_encrypt(caesar_encrypt(s2, 3), -3) == s2
    assert caesar_encrypt(caesar_encrypt(s3, 6), -6) == s3


def test_decypher_file(tmp_path):
    input_path = Path(__file__).parent / "secret_message.txt"
    assert input_path.exists()
    output_path = tmp_path / "output.txt"

    decypher_file(str(input_path), str(output_path))

    with open(output_path, "r") as f:
        lines = f.readlines()
    flat_lines = " ".join(lines)
    assert "the exercise" in flat_lines
    assert "ReDI" in flat_lines
