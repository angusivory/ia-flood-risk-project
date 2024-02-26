
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list



def polyfit(dates, levels, p):
    d0 = dates[0]

