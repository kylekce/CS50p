from fuel import convert, gauge
import pytest

def test_convert():
    # Must return int
    assert convert("3/4") == 75

def test_gauge():
    # Output "E" if less than or equal to 1
    assert gauge(0) == "E"
    assert gauge(1) == "E"

    # Output "F" if more than or equal to 99 
    assert gauge(99) == "F"
    assert gauge(100) == "F"

    # Output the percentage
    assert gauge(75) == "75%"
    assert gauge(75) != "75"

def test_exceptions():
    # ValueError
    with pytest.raises(ValueError):
        convert("x/y")
        convert("three/four")

    # ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
