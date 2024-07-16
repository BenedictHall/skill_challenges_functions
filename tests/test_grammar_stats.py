from lib.grammar_stats import *
import pytest

def test_check_all_combinations():
    grammar = GrammarStats()
    results = []
    results.append(grammar.check("fds"))
    results.append(grammar.check("Food"))
    results.append(grammar.check("food."))
    results.append(grammar.check("Food!"))
    assert results == [False, False, False, True]

def test_check_error_when_empty():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        result = grammar.check("")
    error_message = str(e.value)
    assert error_message == "Can't grammar check an empty text"

def test_check_grammar_percentage():
    grammar = GrammarStats()
    grammar.check("fds")
    grammar.check("Food!")
    grammar.check("Bacon!")
    result = grammar.percentage_good()
    assert result == 67

def test_check_error_when_empty_percentage():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        result = grammar.percentage_good()
    error_message = str(e.value)
    assert error_message == "No texts have been checked yet"