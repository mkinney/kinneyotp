#!python3
# one time pad (aka Vernam Cipher)

class OTP:
    """one time pad class"""

    def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyz", key=""):
        """Constructor"""
        self.alphabet = alphabet
        self.key = key

    def all_valid_letters(self, in_str):
        """Make sure every letter in the in_str is in the alphabet."""
        for i in range(len(in_str)):
            if in_str[i] not in self.alphabet:
                return False
        return True

    def encode(self, in_str):
        """Encode the in_str using the key."""
        encoded = ""
        if len(in_str) != len(self.key):
            return "Text to encode must have the same length as the key.", ""
        if not self.all_valid_letters(in_str):
            return "The string to encode has letters that is not in the alphabet.", ""
        if not self.all_valid_letters(self.key):
            return "The key has letters that is not in the alphabet.", ""
        a = []
        b = []
        for i in range(len(in_str)):
            a.append(self.alphabet.index(in_str[i]))
            b.append(self.alphabet.index(self.key[i]))
        for i in range(len(in_str)):
            encoded += self.alphabet[(a[i] + b[i]) % len(self.alphabet)]
        return "", encoded

    def decode(self, in_str):
        """Decode the in_str using the key."""
        decoded = ""
        if len(in_str) != len(self.key):
            return "Text to decode must have the same length as the key.", ""
        if not self.all_valid_letters(in_str):
            return "The encoded string has letters that is not in the alphabet.", ""
        if not self.all_valid_letters(self.key):
            return "The key has letters that is not in the alphabet.", ""
        a = []
        b = []
        for i in range(len(in_str)):
            a.append(self.alphabet.index(in_str[i]))
            b.append(self.alphabet.index(self.key[i]))
        for i in range(len(in_str)):
            c = a[i] - b[i]
            if c < 0:
                x = len(self.alphabet) + c
            else:
                x = c % 26
            decoded += self.alphabet[x]
        return "", decoded
