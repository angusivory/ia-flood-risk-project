# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from haversine import haversine
from .utils import sorted_by_key  # noqa

"function generates and returns a list of stations, ordered by proximity to specified co-ord point"
def stations_by_distance(stations, p):
    result = []

    #append list with each station name, station town and distance from point p (courtesy of haversine)
    for station in stations:
        result.append((station.name, station.town, haversine(p, station.coord)))

    result = sorted_by_key(result, 2)
    return result


"""function generates and returns a list of stations within a specified radius of a specified co-ord point"""
def stations_within_radius(stations, centre, r):
    those_within_radius = []

    for station in stations:
        r_diff = haversine(centre, station.coord)
        if r_diff < r:
            those_within_radius.append(station.name)      

    return those_within_radius

"""function to generate and return a container of rivers with monitoring stations"""
def rivers_with_station(stations):
    #use a set so that if it comes across a potential duplicate during the for loop, it ignores it
    result = set()
    for station in stations:
        result.add(station.river)
    
    return result

"""function to generate and return a dictionary of <river name> : [stations on river]"""
def stations_by_river(stations):
    result = {}
    for station in stations:
        if not station.river in result:
            result[station.river] = [station.name]
        else:
            result[station.river].append(station.name)

    return result


"""function generates a list of (river, number of stations on river) tuples, then returns the top N entries as required"""
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
    river_tuples = sorted_by_key(river_tuples, 1, True)

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