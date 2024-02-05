# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""

    #Build stations
    stations = build_station_list()

    set_of_rivers = rivers_with_station(stations)
    
    #sets are a pain to sort and slice, hence conversion to list
    list_of_rivers = []
    for x in set_of_rivers:
        list_of_rivers.append(x)
    list_of_rivers.sort()

    print("*** Part (a) ***\n")
    print(len(list_of_rivers), "\n")
    print(list_of_rivers[:10], "\n")

    
    river_dict = stations_by_river(stations)
    for river in river_dict:
        river_dict[river].sort()

    print("*** Part (b) ***\n")
    print(river_dict["River Aire"], "\n")
    print(river_dict["River Cam"], "\n")
    print(river_dict["River Thames"])



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***\n")
    run()
