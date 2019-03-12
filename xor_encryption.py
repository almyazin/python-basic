def xor_encrypt(text, key):
    encrypted = ''
    key_index = 0
    max_key_index = len(key) - 1

    for ch in text:
        encrypted += chr(ord(ch) ^ ord(key[key_index]))
        key_index = key_index + 1 if key_index < max_key_index else 0

    return encrypted


def xor_decrypt(secret_text, key):
    return xor_encrypt(secret_text, key)
