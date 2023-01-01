#!python3
# one time pad (aka Vernam Cipher)

alphabet="abcdefghijklmnopqrstuvwxyz"

def all_valid_letters(in_str, alphabet):
    """Make sure every letter in the in_str is in the alphabet."""
    for i in range(len(in_str)):
        if in_str[i] not in alphabet:
            return False
    return True

def encode(in_str, key):
    """Encode the in_str using the key."""
    encoded = ""
    if len(in_str) != len(key):
        return "Text to encode must have the same length as the key.", ""
    if not all_valid_letters(in_str, alphabet):
        return "The string to encode has letters that is not in the alphabet.", ""
    if not all_valid_letters(key, alphabet):
        return "The key has letters that is not in the alphabet.", ""
    a = []
    b = []
    for i in range(len(in_str)):
        a.append(alphabet.index(in_str[i]))
        b.append(alphabet.index(key[i]))
    for i in range(len(in_str)):
        encoded += alphabet[(a[i] + b[i]) % len(alphabet)]
    return "", encoded

def decode(in_str, key):
    """Decode the in_str using the key."""
    decoded = ""
    if len(in_str) != len(key):
        return "Text to decode must have the same length as the key.", ""
    if not all_valid_letters(in_str, alphabet):
        return "The encoded string has letters that is not in the alphabet.", ""
    if not all_valid_letters(key, alphabet):
        return "The key has letters that is not in the alphabet.", ""
    a = []
    b = []
    for i in range(len(in_str)):
        a.append(alphabet.index(in_str[i]))
        b.append(alphabet.index(key[i]))
    for i in range(len(in_str)):
        c = a[i] - b[i]
        if c < 0:
            x = len(alphabet) + c
        else:
            x = c % 26
        decoded += alphabet[x]
    return "", decoded

if __name__ == "__main__":
    _, encoded = encode("hello", "hbdiq")
    _, decoded = decode("ofote", "hbdiq")
    print("encoded:", encoded)
    print("decoded:", decoded)
