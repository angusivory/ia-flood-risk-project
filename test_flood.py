"""Unit test for the flood module"""

import datetime

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, town_risk_levels, stations_highest_rel_level

# Same data can be used for all tests

stations = [
        MonitoringStation("station1", "measure1", "name1", (1,1), (0, 10), "river1", "town1"), #rel = 1.1
        MonitoringStation("station2", "measure2", "name2", (1,1), (0, 10), "river2", "town1"), #rel = 0.5
        MonitoringStation("station3", "measure3", "name3", (1,1), (0, 10), "river3", "town1"), #rel = None
        MonitoringStation("station4", "measure4", "name4", (1,1), (0, 5), "river4", "town2"), # rel = 3.4
        MonitoringStation("station5", "measure5", "name5", (1,1), (-3, 10), "river5", "town3"), #rel = -1.4615384615384615
        MonitoringStation("station6", "measure6", "name6", (1,1), (0, 10), "river6", "town3"), #rel = 3.4e-05
        MonitoringStation("station7", "measure7", "name7", (1,1), (7, 28), "river7", "town4"), #rel = None
        MonitoringStation("station8", "measure8", "name8", (1,1), (4, 11), "river8", "town4"), #rel = 1.0285714285714285
        MonitoringStation("station9", "measure9", "name9", (1,1), (5, -5), "river9", "town4") #rel = None
]

stations[0].latest_level, stations[0].flood_risk = 11, 3
stations[1].latest_level, stations[0].flood_risk = 5, 2
stations[2].latest_level, stations[0].flood_risk = None, 0
stations[3].latest_level, stations[0].flood_risk = 17, 4
stations[4].latest_level, stations[0].flood_risk = -22, 0
stations[5].latest_level, stations[0].flood_risk = 0.00034, 0
stations[6].latest_level, stations[0].flood_risk = None, 0
stations[7].latest_level, stations[0].flood_risk = 11.2, 3
stations[8].latest_level, stations[0].flood_risk = 6, 0



"""Test for task 2B"""
def test_stations_level_over_threshold():
    test = stations_level_over_threshold(stations, 0.5)
    assert len(test) == 3
    for problem in test:
        assert problem[0].station_id == "station1" or problem[0].station_id == "station4" or problem[0].station_id == "station8"
        assert problem[1] == 1.1 or problem[1] == 1.0285714285714285 or problem[1] == 3.4

"""function should return a dictionary of <town name> : [list of flood risks from each station with flood risk already a parameter]"""
def test_town_risk_levels():    
    test = town_risk_levels(stations)
    assert type(test) == dict
    assert len(test) == 4
    assert len(test["town1"]) == 3
    assert len(test["town2"]) == 1
    assert len(test["town3"]) == 2
    assert len(test["town4"]) == 3

"""function should return the top N stations by relative water level, in form (station, relative water level)"""
def test_stations_highest_rel_level():
    test = stations_highest_rel_level(stations, 4)
    print(test)
    assert len(test) == 4
    for item in test:
        assert item[0].station_id == "station1" or item[0].station_id == "station4" or item[0].station_id == "station8" or item[0].station_id == "station2"
        assert item[1] == 3.4 or item[1] == 1.1 or item[1] == 1.0285714285714285 or item[1] == 0.5