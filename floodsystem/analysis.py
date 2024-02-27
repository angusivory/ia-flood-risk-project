
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list



def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels
    # Using shifted x values, find coefficient of best-fit polynomial f(x) of degree p
    shift = x[0]
    best_fit_coeff = np.polyfit(x - shift, y, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(best_fit_coeff)
    return (poly, shift)


