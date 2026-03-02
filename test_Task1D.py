# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for Task 1D functions"""

from modulefinder import test
from Task1D import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation


def test_rivers_with_station():

    
    s1 = MonitoringStation("id1", "m1", "Station A", (0,0), (0,1), "River X", "Town1")
    s2 = MonitoringStation("id2", "m2", "Station B", (0,0), (0,1), "River Y", "Town2")
    s3 = MonitoringStation("id3", "m3", "Station C", (0,0), (0,1), "River X", "Town3")
    s4 = MonitoringStation("id4", "m4", "Station D", (0,0), (0,1), None, "Town4") 

    stations = [s1, s2, s3, s4]

    rivers = rivers_with_station(stations)

    
    assert "River X" in rivers  
    assert "River Y" in rivers  
    assert None not in rivers   
    assert len(rivers) == 2     


def test_stations_by_river():

    
    s1 = MonitoringStation("id1", "m1", "Station A", (0,0), (0,1), "River X", "Town1")
    s2 = MonitoringStation("id2", "m2", "Station B", (0,0), (0,1), "River Y", "Town2")
    s3 = MonitoringStation("id3", "m3", "Station C", (0,0), (0,1), "River X", "Town3")
    s4 = MonitoringStation("id4", "m4", "Station D", (0,0), (0,1), None, "Town4")  

    stations = [s1, s2, s3, s4]

    river_dict = stations_by_river(stations)


    assert "River X" in river_dict
    assert "River Y" in river_dict
    assert None not in river_dict  

    
    river_x_names = [s.name for s in river_dict["River X"]]
    river_y_names = [s.name for s in river_dict["River Y"]]

    assert sorted(river_x_names) == ["Station A", "Station C"]
    assert sorted(river_y_names) == ["Station B"]

