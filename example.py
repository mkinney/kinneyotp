#!python

from kinneyotp import OTP, Key

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

text = "HELLO"
k = Key(alphabet=alphabet, length=len(text))
mykey=k.generated
a = OTP(alphabet=alphabet, key=mykey)
_, encoded = a.encode(text)
print("text:", text, "key:", mykey, "encoded:", encoded)
