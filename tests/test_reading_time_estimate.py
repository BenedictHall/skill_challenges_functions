import pytest

from lib.reading_time_estimate import *

def test_reading_100_words():
    result = reading_time_estimate("a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j a b, c d e f g h i j ")
    assert result == 0.5

def test_reading_no_text():
    with pytest.raises(Exception) as e:
        result = reading_time_estimate("")
    error_message = str(e.value)
    assert error_message == "Can't read an empty text"