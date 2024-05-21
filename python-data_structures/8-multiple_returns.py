#!/usr/bin/python3
def multiple_returns(sentence):
    legth = 0
    for i in sentence:
        legth += 1
    
    return legth, sentence[0]
