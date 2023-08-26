from plates import is_valid

# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def test_is_valid_1():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

# All vanity plates must start with at least two letters
def test_is_valid_2():
    assert is_valid("ABCDEF") == True
    assert is_valid("A12345") == False
    assert is_valid("123456") == False

# Numbers cannot be used in the middle of a plate; they must come at the end
def test_is_valid_3():
    assert is_valid("1ABCDE") == False
    assert is_valid("ABCDE1") == True
    assert is_valid("ABC1DE") == False

# The first number used cannot be a ‘0’.
def test_is_valid_4():
    assert is_valid("ABC123") == True
    assert is_valid("AB0123") == False

# No periods, spaces, or punctuation marks are allowed.
def test_is_valid_5():
    assert is_valid("A123.B") == False
    assert is_valid("AB,12C") == False
    assert is_valid("AB/#'!") == False
    assert is_valid("      ") == False
