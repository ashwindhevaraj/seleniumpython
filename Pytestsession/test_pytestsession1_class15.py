import pytest
def test_m1():
    a=3
    b=4
    assert a+1==b
def test_m2():
    a=3
    b=4
    assert a==b, "a is not close to b"
def test_m3():
    assert True
def test_m4():
    a='selenium'
    assert a.upper()=='SELENIUM'
