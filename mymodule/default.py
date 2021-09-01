#! /usr/bin/env python
import numpy as np


def hard_compute(number,
                 word,
                 option=None
                 ):
    """
    Silly function just for examples
    """
    if not option:
        return number
    result = '.'.join([word, str(option)])
    return result


def deg2hms(x):
    """
    Format decimal degrees into sexigessimal HH:MM:SS.SS

    Parameters
    ----------
    x : float
        Angle in degrees. Assumed to be in [-360,360]

    Returns
    -------
    hms : string
        Sexigessimal representation of x, in the format HH:MM:SS.SS
        If x is np.nan, or np.inf then return "XX:XX:XX.XX" instead
    """
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
