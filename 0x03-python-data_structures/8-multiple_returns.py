#!/usr/bin/python3
def multiple_returns(sentence):
    t_tuple = ()
    if len(sentence) == 0:
        t_tuple = 0, "None"
    else:
        t_tuple = len(sentence), sentence[0]
    return t_tuple
