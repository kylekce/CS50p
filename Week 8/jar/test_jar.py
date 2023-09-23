from jar import Jar
from pytest import raises

def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    j = Jar(10)
    assert j.capacity == 10
    assert j.size == 0

def test_str():
    j = Jar()
    assert str(j) == ""

    j.deposit(5)
    assert str(j) == "🍪🍪🍪🍪🍪"

    j.withdraw(2)
    assert str(j) == "🍪🍪🍪"

def test_deposit():
    j = Jar()

    j.deposit(5)
    assert j.size == 5

    j.deposit(5)
    assert j.size == 10

    with raises(ValueError):
        j.deposit(5)

def test_withdraw():
    j = Jar()

    j.deposit(5)
    j.withdraw(2)
    assert j.size == 3

    with raises(ValueError):
        j.withdraw(5)
