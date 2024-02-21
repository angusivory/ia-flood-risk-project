import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # sort stations[] by relative water level, avoiding errors thrown by station.relative_water_level() returning None
    valid_stations = []
    invalid_stations = []
    for station in stations:
        try:
            fl_level = float(MonitoringStation.relative_water_level(station))
            valid_stations.append(station)
        except:
            invalid_stations.append(station)

    valid_stations.sort(key=lambda x: MonitoringStation.relative_water_level(x), reverse=True)
    stations = valid_stations + invalid_stations

    # result is the 5 stations with greatest current relative water level
    stations_of_concern = stations[:5]

    # get 10-day water level history for these 5
    histories = []
    dt = 10

    for worry in stations_of_concern:
        dates, levels = fetch_measure_levels(worry.measure_id, dt=datetime.timedelta(days=dt))
        histories.append([worry, dates, levels])
   
    # plot each history
    for item in histories:
        plot_water_levels(item[0], item[1], item[2])


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
