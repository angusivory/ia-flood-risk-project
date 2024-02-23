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

def town_risk_levels(stations):
    result = {}

    for station in stations:
        if station.town in result:
            result[station.town].append(station.flood_risk)
        else:
            result[station.town] = [station.flood_risk]

    return result