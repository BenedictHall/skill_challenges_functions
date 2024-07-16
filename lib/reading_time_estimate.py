#describe problem
#wants an estimate of time it would take to read a text, given he can read 200 words a minute

#function signature
"""
def reading_time_estimate(text):
    splits text into words, and calculates time taken
    parameter: the text given, string
    return: float, number of minutes it would take
    """

def reading_time_estimate(text):
    if text == "":
        raise Exception("Can't read an empty text")
    words = text.split(" ")
    words = list(filter(lambda x: x != "", words))
    return len(words)/200