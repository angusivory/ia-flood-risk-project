"""This module contains a collection of functions related to
water level data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation


"""function returns stations with a certain relative water level via a list of tuples"""
def stations_level_over_threshold(stations, tol):
    result = []

    for station in stations:
        relative_water_level = MonitoringStation.relative_water_level(station)
        #try and except loop to catch inconsistent water level stations
        try:
            if relative_water_level > tol:
                result.append((station, relative_water_level))
        except:
            #'None' is returned as the water level data for this station is inconsistent
            pass
    result = sorted_by_key(result, 1, True)
    return result

"""function returns a dictionary of <town name> : [list of flood risks from each station]"""
def town_risk_levels(stations):
    result = {}

    for station in stations:
        if station.town in result:
            result[station.town].append(station.flood_risk)
        else:
            result[station.town] = [station.flood_risk]

    return result

"""function to return the top N stations by relative waterlevel, in form (station, relative water level)"""
def stations_highest_rel_level(stations, N):
    result = []

    for station in stations:
        relative_water_level = MonitoringStation.relative_water_level(station)
        result.append((station, relative_water_level))

    # Remove stations with relative_water_level = None as that messes up the sorting
    data_fine = []
    data_bad = []
    for x in result:
        if x[1] != None:
            data_fine.append(x)
        else:
            data_bad.append(x)

    data_fine = sorted_by_key(data_fine, 1, reverse=True)
    
    # Recombine lists
    result = data_fine + data_bad
    return result[:N]
