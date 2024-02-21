import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

"""Task 2G requires us to list the *towns* where we consider flooding risk to be the greatest, rating the risk at 'severe', 'high', 'moderate' or 'low'

Analytical tools that might come in useful are:
- flood.stations_level_over_threshold() -> determine thresholds for different risk levels
- geo.stations_by_river() -> if a river is flooding somewhere, figure out which stations (towns) are on it
- update_water_level() --> current water levels
- fetch_measure_levels() --> get a water level history to find trends and predict the future

"""

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    #update_water_levels(stations)



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
