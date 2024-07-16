"""
1. Describe the problem
verify text starts with capital letter, ends with suitable sentence ending punctuation

2. Design function signature

def grammar_verifier(text):
    checks first letter is capitalised, check it ends with reasonable punctuation
    
    parameters: 
    text : string containing words
    
    returns:
    boolean to show whether the checks were true
    
    
3. Test examples

returns false when neither is true

returns false when just capitalization is true

returns false when just punctuation is true

returns true when both are true

4. Implementation
"""
def grammar_verifier(text):
    return text[0].isupper() and text[-1] in ".?!"