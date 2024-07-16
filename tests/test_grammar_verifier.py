from lib.grammar_verifier import *

def test_grammar_verifier_bad_both():
    result = grammar_verifier("fdsf")
    assert result == False

def test_grammar_verifier_punc_bad():
    result = grammar_verifier("Cheese")
    assert result == False

def test_grammar_verifier_capt_bad():
    result = grammar_verifier("balling.")
    assert result == False

def test_grammar_verifier_good_both():
    result = grammar_verifier("Balling!")
    assert result == True