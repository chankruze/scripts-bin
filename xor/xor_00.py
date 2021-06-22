# XOR_KEY = ????


def encrypt(value, key):
    return [chr(ord(ch) ^ key) for ch in value]


if __name__ == "__main__":
    plain_text = "Abhinav"
    plain_text2 = "Mayank"
    enc = encrypt(plain_text, XOR_KEY)
    print(f"enc = {enc}")
    enc2 = encrypt(plain_text2, XOR_KEY)
    print(f"enc2 = {enc}")

    print([chr(ord(a) ^ ord(b)) for (a, b) in zip(enc, enc2)])
    print([chr(ord(a) ^ ord(b)) for (a, b) in zip(plain_text, plain_text2)])
