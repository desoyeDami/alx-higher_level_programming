#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) is None:
        return length, None
    else:
        first = sentence[0]
        return length, first
