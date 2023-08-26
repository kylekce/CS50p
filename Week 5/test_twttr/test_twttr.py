from twttr import shorten

def test_lower_words():
    assert shorten("apple") == "ppl"
    assert shorten("cat") == "ct"

def test_upper_words():
    assert shorten("APPLE") == "PPL"
    assert shorten("CAT") == "CT"

def test_numbers():
    assert shorten("1") == "1"
    assert shorten("Apple25") == "ppl25"

def test_punctuations():
    assert shorten("...twitter, and fb") == "...twttr, nd fb"
