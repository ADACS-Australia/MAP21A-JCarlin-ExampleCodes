#! /usr/bin/env python

def hard_compute(number,
                word,
                option=None
                ):
    if not option:
        return number
    result = '.'.join([word,str(option)])
    return result
