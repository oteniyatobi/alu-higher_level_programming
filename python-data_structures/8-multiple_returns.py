#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple containing the length of the sentence and its first character."""
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    return (len(sentence), first_char)
