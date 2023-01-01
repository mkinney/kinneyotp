from otp import all_valid_letters

def test_all_valid_letters_no_input():
    assert all_valid_letters("", "abc") == True

def test_all_valid_letters_a_letter_not_in_alphabet():
    assert all_valid_letters("abc", "") == False
    assert all_valid_letters("abc", "ab") == False

def test_all_valid_letters_valid_input():
    assert all_valid_letters("abcabc", "abcdefgh") == True
