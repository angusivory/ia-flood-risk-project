import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stations_of_concern = stations_highest_rel_level(stations,5)


    for item in stations_of_concern:
        dates, levels = fetch_measure_levels(item[0].measure_id, dt=datetime.timedelta(days=2))

        plot_water_level_with_fit(item[0], dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
