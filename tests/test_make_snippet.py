from lib.make_snippet import *

def test_5_or_less():
    result = make_snippet("short")
    assert result == "short"

def test_more_than_5():
    result = make_snippet("man this string is long")
    assert result == "man t..."