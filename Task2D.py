import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """Plot water levels against time and include typical range lines."""

    # Plot water level data
    plt.plot(dates, levels, label="Water level")

    # Plot typical range if available
    if station.typical_range is not None:
        low, high = station.typical_range

        # Horizontal lines for typical low/high
        plt.hlines(low, dates[0], dates[-1], linestyles="dashed", label="Typical low")
        plt.hlines(high, dates[0], dates[-1], linestyles="dashed", label="Typical high")

    # Labels and formatting
    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Copyright (C) 2018 Garth N. Wells
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels


def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest water levels
    update_water_levels(stations)

    # Get 5 stations with highest relative water levels
    highest_stations = stations_highest_rel_level(stations, 5)

    # Time period (past 10 days)
    dt = datetime.timedelta(days=10)

    # Plot water levels for each station
    for station in highest_stations:

        # Fetch level history
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        if dates and levels:
            print("Plotting:", station.name)
            plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()