from lib.count_words import *

def test_length():
    result = count_words("bacon")
    assert result == 5
    