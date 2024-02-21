"""Unit test for the flood module"""

import datetime

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

"""Test for task 2B"""
def test_stations_level_over_threshold():
    stations = [
        MonitoringStation("station1", "measure1", "name1", (1,1), (0, 10), "river1", "town1"),
        MonitoringStation("station2", "measure2", "name2", (1,1), (0, 10), "river2", "town2"),
        MonitoringStation("station3", "measure3", "name3", (1,1), (0, 10), "river3", "town3"),
        MonitoringStation("station4", "measure4", "name4", (1,1), (0, 5), "river4", "town4"),
        MonitoringStation("station5", "measure5", "name5", (1,1), (-3, 10), "river5", "town5"),
        MonitoringStation("station6", "measure6", "name6", (1,1), (0, 10), "river6", "town6"),
        MonitoringStation("station7", "measure7", "name7", (1,1), (7, 28), "river7", "town7"),
        MonitoringStation("station8", "measure8", "name8", (1,1), (4, 11), "river8", "town8"),
        MonitoringStation("station9", "measure9", "name9", (1,1), (5, -5), "river9", "town9")
    ]

    stations[0].latest_level = 11
    stations[1].latest_level = 5
    stations[2].latest_level = None
    stations[3].latest_level = 17
    stations[4].latest_level = -22
    stations[5].latest_level = 0.00034
    stations[6].latest_level = None
    stations[7].latest_level = 11.2
    stations[8].latest_level = 6

    test = stations_level_over_threshold(stations, 0.5)
    assert len(test) == 3
    for problem in test:
        assert problem[0].station_id == "station1" or problem[0].station_id == "station4" or problem[0].station_id == "station8"
        assert problem[1] == 1.1 or problem[1] == 1.0285714285714285 or problem[1] == 3.4