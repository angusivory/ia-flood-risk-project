# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    #Build stations
    stations = build_station_list()

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    inconsistent_station_names = []
    for x in inconsistent_stations:
        inconsistent_station_names.append(x.name)
        
    inconsistent_station_names.sort()
    print(inconsistent_station_names)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
