# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from .utils import sorted_by_key  # noqa


#function for task 1C to be inserted after Adhvika's task 1B module

def stations_within_radius(stations, centre, r, in_km=True):
    those_within_radius = []

    #this converts km into degrees of long/lat, unless the user has already done that.
    if in_km == True:
        r *= 360/40000

    for station in stations:
        x_diff = station.coord[0] - centre[0]
        y_diff = station.coord[1] - centre[1]
        r_diff = math.sqrt(x_diff**2 + y_diff**2)
        if r_diff < r:
            those_within_radius.append(station.name)      

    return those_within_radius
