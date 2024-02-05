"""Unit test for the geo module"""

import datetime

from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation


"""Test for task 1B"""
def test_stations_by_distance():
    stations = [
        MonitoringStation("here", "001", "His Abode", (1,1), (0, 20), "Bin Brook", "Heaven"),
        MonitoringStation("there", "002", "The mojo dojo casa house", (50.3, 17), (0, 20), "The Nile", "The Temple of Doom"),
        MonitoringStation("everywhere", "003", "Top Secret", (-89, -89), (0, 20), "The Ganges", "Cloud 9"),
        MonitoringStation("nowhere", "004", "Seb's jazz bar", (16, 37.44), (0, 20), "The Yangzte", "Lalaland")
    ]

    test = stations_by_distance(stations, (0,0))
    assert test[0][0] == "His Abode"
    assert test[1][0] == "Seb's jazz bar"
    assert test[2][0] == "The mojo dojo casa house"
    assert test[3][0] == "Top Secret"

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
def test_rivers_with_station():
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

    test = rivers_with_station(stations)
    assert "thames" in test
    assert "hudson" in test
    assert "bascall" in test
    assert "jammy" in test
    assert len(test) == 4

def test_stations_by_river():
    stations = [
        MonitoringStation("numero uno", "001", "one", (1,1), (0, 20), "thames", "t1"),
        MonitoringStation("numero 2", "002", "two", (1.009, 1), (0, 20), "hudson", "t2"),
        MonitoringStation("numero 3", "003", "three", (1.009, 1.10), (0, 20), "hudson", "t3"),
        MonitoringStation("numero 4", "004", "four", (1.009, 1.10), (0, 20), "thames", "t3"),
        MonitoringStation("numero 5", "005", "five", (1.009, 1.10), (0, 20), "bascall", "t3"),
        MonitoringStation("numero 6", "006", "six", (1.009, 1.10), (0, 20), "hudson", "t3"),
        MonitoringStation("numero 7", "007", "seven", (1.009, 1.10), (0, 20), "jammy", "t3"),
        MonitoringStation("numero 8", "008", "eight", (1.009, 1.10), (0, 20), "jammy", "t3")
    ]

    test = stations_by_river(stations)
    assert type(test) == dict
    assert len(test["thames"]) == 2
    assert len(test["hudson"]) == 3
    assert len(test["bascall"]) == 1
    assert len(test["jammy"]) == 2

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