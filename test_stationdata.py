# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

from floodsystem.stationdata import build_station_list, update_water_levels, assign_risk_categories
from floodsystem.station import MonitoringStation


def test_build_station_list():
    """Test building list of stations"""
    station_list = build_station_list()
    assert len(station_list) > 0


def test_update_level():
    """Test update to latest water level"""

    # Build list of stations
    stations = build_station_list()
    for station in stations:
        assert station.latest_level is None

    # Update latest level data for all stations
    update_water_levels(stations)
    counter = 0
    for station in stations:
        if station.latest_level is not None:
            counter += 1

    assert counter > 0

"""function should return risk categories attached to station objects"""
def test_assign_risk_categories():
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

    stations[0].latest_level = 11
    stations[1].latest_level = 5
    stations[2].latest_level = None
    stations[3].latest_level = 17
    stations[4].latest_level = -22
    stations[5].latest_level = 0.00034
    stations[6].latest_level = None
    stations[7].latest_level = 11.2
    stations[8].latest_level = 6

    thresholds = [0.4, 0.8, 1.5]
    test = assign_risk_categories(stations, thresholds)
    assert len(test) == 9
    assert test[0].flood_risk == 3
    assert test[2].flood_risk == 0
