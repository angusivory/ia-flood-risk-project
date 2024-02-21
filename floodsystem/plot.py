"""This module contains a collection of functions related to
water level data.

"""
import matplotlib.pyplot as plt
import numpy as np

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation

"""function to display, using matplotlib, water level vs time for a given station"""
def plot_water_levels(station, dates, levels):
    # Plot
    typical_low = np.full(len(dates), station.typical_range[0])
    typical_high = np.full(len(dates), station.typical_range[1])

    print("{} - low: {}, high: {}, latest: {}, relative: {}".format(station.name, station.typical_range[0], station.typical_range[1], station.latest_level, MonitoringStation.relative_water_level(station)))

    plt.plot(dates, levels)
    plt.plot(dates, typical_low)
    plt.plot(dates, typical_high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()