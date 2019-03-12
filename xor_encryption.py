def xor_encrypt(text, key):
    encrypted = ''

    for idx, ch in enumerate(text):
        encrypted += chr(ord(ch) ^ ord(key[idx % len(key)]))

    return encrypted


def xor_decrypt(secret_text, key):
    return xor_encrypt(secret_text, key)
