import datetime

from floodsystem.stationdata import build_station_list, update_water_levels, assign_risk_categories
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius_returns_object
from floodsystem.flood import town_risk_levels

"""Task 2G requires us to list the *towns* where we consider flooding risk to be the greatest, rating the risk at 'severe', 'high', 'moderate' or 'low'

Analytical tools that might come in useful are:
- flood.stations_level_over_threshold() -> determine thresholds for different risk levels
- geo.stations_by_river() -> if a river is flooding somewhere, figure out which stations (towns) are on it
- update_water_level() --> current water levels
- fetch_measure_levels() --> get a water level history to find trends and predict the future

Hence, the logic:

VARIABLES
risk_radius = int
categories = {1: "low", 2: "moderate", 3: "high", 4: "severe"}
severe > 1.2
0.8 < high <= 1.2
0.4 < moderate <= 0.8
low <= 0.4

1. determine risk level based off level_over_threshold()
2. for any stations rated 'severe', up the risk level of any station (i) on the same river AND (ii) within 5km
3a. rank by category, then water level. then print towns on severe, add to a set so no duplicates
3b. OR make a dictionary of town : {level, level, level, level, level} and either average OR award points based on how many 4s and 3s
4+. elegantly numerically differentiate the historical water level data to see whether the water levels of at-risk stations are increasing or decreasing.

NB: if we had more time, it would cut processing time to add self.relative_water_level as a class method/parameter, maybe called every time fetch_latest_water_levels is run, to avoid having to call the function every time we want a comparison

"""

def run():
    # Variables
    categories = {0: "undefined", 1: "low", 2: "moderate", 3: "high", 4: "severe"}
    thresholds = [0.4, 0.8, 1.5]
    risk_radius = 1
    severe_stations = []
    new_severe_stations = []
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Assign flood risk levels to all stations
    assign_risk_categories(stations, thresholds)


    for station in stations:
        if station.flood_risk == 4:
            severe_stations.append(station)
        if station.relative_water_level() == None:
            stations.remove(station)
    
    # Add stations that are on the same river and within 'risk_radius' km
    for station in severe_stations:
        nearby_stations = stations_within_radius_returns_object(stations, station.coord, risk_radius)
        
        for possible in nearby_stations:
            if possible.river == station.river:
                possible.flood_risk += 1
                if possible.flood_risk >= 4:
                    possible.flood_risk = 4
                    new_severe_stations.append(possible)
                    stations.remove(possible)

    stations = stations + new_severe_stations

    # Sort by category, then relative water level
    stations.sort(key=lambda x: (x.flood_risk, x.relative_water_level()), reverse=True)

    towns_at_risk = town_risk_levels(stations)
    
    print("Towns at risk:\n")
    for town in towns_at_risk:
        average = sum(towns_at_risk[town])/len(towns_at_risk[town])
        if average > 3:
            print("{}: average level of {} ({} stations)".format((town), average, len(towns_at_risk[town])))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
