"""Unit test for the geo module"""

import datetime

#from floodsystem.geo import <task1b module>
from floodsystem.geo import stations_within_radius, rivers_by_station_number

#def task 1b test

from floodsystem.stationdata import build_station_list, update_water_levels


"""Test building list of stations"""
station_list = build_station_list()
print(station_list[:6])    


def test_sort_stations_within_radius():
    test_stations = []
    expected_response = []
    pass

def test_rivers_by_station_numbers():
    pass