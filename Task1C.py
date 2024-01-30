# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    #Define variables
    cam_centre = (52.2053, 0.1218)
    radius = 10

    #Build stations
    stations = build_station_list()


    cam_ten = stations_within_radius(stations, cam_centre, radius)
    cam_ten.sort()
    print(cam_ten)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
