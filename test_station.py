# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

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