#! /usr/bin/env python
import numpy as np

def hard_compute(number,
                word,
                option=None
                ):
    if not option:
        return number
    result = '.'.join([word,str(option)])
    return result

def deg2hms(x):
    if not np.isfinite(x):
        return 'XX:XX:XX.XX'
    # wrap negative RA's
    if x < 0:
        x += 360
    x /= 15.0
    h = int(x)
    x = (x - h) * 60
    m = int(x)
    s = (x - m) * 60
    return f"{h:02d}:{m:02d}:{s:05.2f}"

