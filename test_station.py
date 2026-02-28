# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    # Test consistent range
    trange1 = (-2.3, 3.4445)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    assert s1.typical_range_consistent() == True

    # Test inconsistent range
    trange2 = (3.4445, -2.3)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    assert s2.typical_range_consistent() == False

    # Test None range
    trange3 = None
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    assert s3.typical_range_consistent() == False


def test_inconsistent_typical_range_stations():

    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    trange1 = (-2.3, 3.4445)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)

    trange2 = (3.4445, -2.3)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)

    trange3 = None
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)

    stations = [s1, s2, s3]

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert s1 not in inconsistent_stations
    assert s2 in inconsistent_stations
    assert s3 in inconsistent_stations
