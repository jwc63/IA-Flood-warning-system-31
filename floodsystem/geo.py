# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """returns a list of (station, distance) tuples sorted by distance"""

    station_distance = []

    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))

    return sorted_by_key(station_distance, 1)


def stations_within_radius(stations, centre, r):
    """returns a list of all stations within radius r of a geographic coordinate x"""

    stations_in_radius = []

    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_in_radius.append(station)

    return stations_in_radius