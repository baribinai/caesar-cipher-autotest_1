from solution import caesar_cipher


def test_caesar_cipher_basic_example():
    assert caesar_cipher("Doggy", 5) == "ItllD"


def test_caesar_cipher_phrase_example():
    assert caesar_cipher("Python is the BEST!", 20) == "jSNBIH CM NBy VYmn!"


def test_caesar_cipher_keeps_spaces_punctuation_and_digits():
    assert caesar_cipher("Hello, World! 123", 3) == "Khoor, Zruog! 123"


def test_caesar_cipher_with_zero_key():
    assert caesar_cipher("Python is the BEST!", 0) == "Python is the BEST!"


def test_caesar_cipher_with_large_key():
    assert caesar_cipher("abcXYZ", 52) == "abcXYZ"


def test_caesar_cipher_with_negative_key():
    assert caesar_cipher("abcXYZ", -1) == "ZabWXY"


def test_caesar_cipher_empty_string():
    assert caesar_cipher("", 5) == ""


def test_caesar_cipher_only_non_letters():
    assert caesar_cipher("123 !?,.-", 10) == "123 !?,.-"
