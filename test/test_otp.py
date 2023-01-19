from kinneyotp import OTP

def test_all_valid_letters_no_input():
    a = OTP()
    assert a.all_valid_letters("") == True

def test_all_valid_letters_a_letter_not_in_alphabet():
    a = OTP()
    assert a.all_valid_letters(".") == False

def test_all_valid_letters_valid_input():
    a = OTP()
    assert a.all_valid_letters("ABCABC") == True

def test_encode_no_key():
    a = OTP()
    msg, val = a.encode("hello")
    assert msg != ""
    assert val == ""

def test_encode_valid_key_default_alphabet():
    a = OTP(key="HBDIQ")
    msg, val = a.encode("HELLO")
    assert msg == ""
    assert val == "OFOTE"

def test_encode_letter_text_to_encode_has_letter_not_in_alphabet():
    a = OTP(alphabet="abc", key="abc")
    msg, val = a.encode("foo")
    assert msg != ""
    assert val == ""

def test_encode_letter_key_has_letter_not_in_alphabet():
    a = OTP(alphabet="abc", key="def")
    msg, val = a.encode("aaa")
    assert msg != ""
    assert val == ""

def test_decode_valid_key_default_alphabet():
    a = OTP(key="HBDIQ")
    msg, val = a.decode("OFOTE")
    assert msg == ""
    assert val == "HELLO"

def test_decode_key_is_longer():
    a = OTP(key="ABC")
    msg, val = a.decode("A")
    assert msg == ""
    assert val == "A"

def test_decode_key_and_text_are_same_length():
    a = OTP(key="ABC")
    msg, val = a.decode("ABC")
    assert msg == ""
    assert val == "AAA"

def test_decode_key_is_not_long_enough():
    a = OTP(key="A")
    msg, val = a.decode("ABC")
    assert msg != ""
    assert val == ""

def test_decode_letter_in_decode_string_not_in_alphabet():
    a = OTP(key="ABC")
    msg, val = a.decode("abc")
    assert msg != ""
    assert val == ""

def test_decode_key_has_letters_not_in_alphabet():
    a = OTP(key="abc")
    msg, val = a.decode("ABC")
    assert msg != ""
    assert val == ""

def test_with_different_alphabet():
    a = OTP(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!", key="KJJGHV")
    e = "HELLO."
    msg, val = a.encode(e)
    assert msg == ""
    assert val == "RNURVR"
    msg2, val2 = a.decode(val)
    assert msg2 == ""
    assert val2 == e

def test_encode_matches_decode():
    a = OTP(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!", key="9!KOOL.")
    e = "TES?ING"
    msg, val = a.encode(e)
    assert msg == ""
    msg2, val2 = a.decode(val)
    assert msg2 == ""
    assert val2 == e
