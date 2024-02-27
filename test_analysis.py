"""Unit test for the flood module"""

import datetime
import matplotlib
import matplotlib.dates
from floodsystem.analysis import polyfit

"""function should return a tuple (poly1d, shift)"""
def test_polyfit():
    dates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    levels = [2, 4, 6, 8, 10, 12, 9, 7, 5]
    test = polyfit(dates, levels, 4)
    assert tuple(test)