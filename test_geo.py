"""Unit test for the geo module"""

import datetime

from floodsystem.geo import stations_within_radius, rivers_by_station_number
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

from floodsystem.stationdata import build_station_list, update_water_levels

"""Test for task 1B"""

"""Test for task 1C"""
def test_sort_stations_within_radius():
    stations = [
        MonitoringStation("same coords", "001", "sc", (1,1), (0, 20), "r1", "t1"),
        MonitoringStation("within", "002", "w/i", (1.009, 1), (0, 20), "r2", "t2"),
        MonitoringStation("without", "003", "w/o", (1.009, 1.10), (0, 20), "r3", "t3")
    ]

    test = stations_within_radius(stations, (1,1), 5)
    assert isinstance(test, list)
    assert len(test) == 2
    assert test[0] == "sc" or test[1] == "sc"
    assert test[0] == "w/i" or test[1] == "w/i"
    

"""Test for task 1D"""

"""Test for task 1E"""
def test_rivers_by_station_number():
    stations = [
        MonitoringStation("1st highest", "001", "one", (1,1), (0, 20), "thames", "t1"),
        MonitoringStation("2nd highest", "002", "two", (1.009, 1), (0, 20), "hudson", "t2"),
        MonitoringStation("3rd highest", "003", "three", (1.009, 1.10), (0, 20), "hudson", "t3"),
        MonitoringStation("4th highest", "004", "four", (1.009, 1.10), (0, 20), "thames", "t3"),
        MonitoringStation("5th highest", "005", "five", (1.009, 1.10), (0, 20), "bascall", "t3"),
        MonitoringStation("6th highest", "006", "six", (1.009, 1.10), (0, 20), "hudson", "t3"),
        MonitoringStation("7th highest", "007", "seven", (1.009, 1.10), (0, 20), "jammy", "t3"),
        MonitoringStation("8th highest", "008", "eight", (1.009, 1.10), (0, 20), "jammy", "t3")
    ]
    test = rivers_by_station_number(stations, 3)
    assert test == [('hudson', 3), ('thames', 2), ('jammy', 2)]

"""Test for task 1F"""
def test_inconsistent_typical_range_stations():
    stations = [
        MonitoringStation("1st highest", "001", "one", (1,1), (0.1, 2.50), "thames", "t1"),
        MonitoringStation("2nd highest", "002", "two", (1, 1), (0, 203), "hudson", "t2"),
        MonitoringStation("3rd highest", "003", "three", (1, 1.10), (2.1, 0.74), "hudson", "t3"),
        MonitoringStation("4th highest", "004", "four", (1, 1.10), None, "thames", "t3"),
        MonitoringStation("5th highest", "005", "five", (1, 1.10), (0, 20), "bascall", "t3"),
        MonitoringStation("6th highest", "006", "six", (1, 1.10), None, "hudson", "t3"),
        MonitoringStation("7th highest", "007", "seven", (1, 1.10), (0, 20), "jammy", "t3"),
        MonitoringStation("8th highest", "008", "eight", (1, 1.10), None, "jammy", "t3"),
    ]
    test = inconsistent_typical_range_stations(stations)
    for i, x in enumerate(test):
        test[i] = x.name
    test.sort()
    assert test == ["eight", "four", "six", "three"]