from string import ascii_letters as alpha


def caesar_cipher(data: str, key: int) -> str:
    cipher_data = ""
    len_alpha = len(alpha)

    for ch in data:
        if ch in alpha:
            cipher_data += alpha[(alpha.index(ch) + key) % len_alpha]
        else:
            cipher_data += ch

    return cipher_data
