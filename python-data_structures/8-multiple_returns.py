#!/usr/bin/python3
def multiple_returns(sentence):
    """Return length and first character."""
    first = sentence[0] if sentence else None
    return (len(sentence), first)
