import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.analysis import polyfit

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for i,j in stations_highest_rel_level(stations,5):
        stationlist = stationlist + [i]

        print(stationlist)

    five_station = 

    for station in five_station:

        time = 2
        p = 4

        dates, levels = fetch_measure_levels(station.measure_id, time=datetime.timedelta(days=time))

        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
