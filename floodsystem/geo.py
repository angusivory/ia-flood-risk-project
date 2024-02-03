# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from .utils import sorted_by_key  # noqa


#function for task 1B to be inserted here

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

#function for task 1D to be inserted here

def rivers_by_station_number(stations, N):
    river_dict = {}
    river_tuples = []

    """Generate a dictionary of <river> : <number of stations>"""
    for station in stations:
        if station.river in river_dict:
            river_dict[station.river] += 1
        else:
            river_dict[station.river] = 1

    """Convert dictionary to list of tuples"""
    river_tuples = [(river, value) for river, value in river_dict.items()]

    """Sort list of tuples by second element, i.e. <number of stations>"""
    river_tuples.sort(key = lambda x: x[1], reverse=True)     
    
    """Iterate through tuples and return the ones with the N highest number of stations"""
    river_tuples_slice = []
    done = False
    counter = 0
    while done == False:
        if counter < (N):
            river_tuples_slice.append(river_tuples[counter])
        else:
            if river_tuples[counter][1] == river_tuples_slice[N-1][1]:
                river_tuples_slice.append(river_tuples[counter])
            else:
                done = True
        counter += 1
    
    return river_tuples_slice