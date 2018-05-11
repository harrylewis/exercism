alphabet = "abcdefghijklmnopqrstuvwxyz"


def rotate(text, key):
    transpose = ""
    cipher = ""

    for char in text:
        if char.isalpha():
            transpose = (list(alphabet).index(char.lower()) + key) % 26
            cipher += alphabet[transpose] if not char.isupper() else alphabet[transpose].upper()
        else:
            cipher += char

    return cipher
