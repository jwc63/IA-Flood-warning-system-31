# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from Task1D import stations_by_river
from Task1E import rivers_by_station_number
from floodsystem.station import MonitoringStation


def test_rivers_by_station_number():
    """Test rivers_by_station_number() function"""

    # Create example stations
    s1 = MonitoringStation("id1", "m1", "Station A", (0,0), (0,1), "River X", "Town1")
    s2 = MonitoringStation("id2", "m2", "Station B", (0,0), (0,1), "River Y", "Town2")
    s3 = MonitoringStation("id3", "m3", "Station C", (0,0), (0,1), "River X", "Town3")
    s4 = MonitoringStation("id4", "m4", "Station D", (0,0), (0,1), "River Z", "Town4")
    s5 = MonitoringStation("id5", "m5", "Station E", (0,0), (0,1), "River Z", "Town5")
    s6 = MonitoringStation("id6", "m6", "Station F", (0,0), (0,1), "River Y", "Town6")

    stations = [s1, s2, s3, s4, s5, s6]

    top_rivers = rivers_by_station_number(stations, 2)

   
    river_names = [river for river, count in top_rivers]
    river_counts = {river: count for river, count in top_rivers}

    assert "River X" in river_names
    assert "River Y" in river_names
    assert "River Z" in river_names

   
    assert river_counts["River X"] == 2
    assert river_counts["River Y"] == 2
    assert river_counts["River Z"] == 2

    
    assert len(top_rivers) == 3
