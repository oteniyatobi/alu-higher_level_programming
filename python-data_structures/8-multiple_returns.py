#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple containing the length of the sentence and its first character."""
    first_char = sentence[0] if sentence else None
    return (len(sentence), first_char)
