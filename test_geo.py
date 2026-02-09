from floodsystem import geo
from floodsystem.station import MonitoringStation
from haversine import haversine

def test_stations_by_distance():
    """Tests stations_by_distance"""

    A = MonitoringStation('idA', 'measureA', 'A', (0, 0), (0, 1), 'riverA', 'townA')
    B = MonitoringStation('idB', 'measureB', 'B', (1, 1), (0, 1), 'riverB', 'townB')
    C = MonitoringStation('idC', 'measureC', 'C', (-2, -2), (0, 1), 'riverC', 'townC')

    stations = [A, B, C]
    p = (0, 0)

    result = geo.stations_by_distance(stations, p)
    assert result[0][0] == A
    assert result[1][0] == B
    assert result[2][0] == C

def test_stations_within_radius():
    """Tests stations_within_radius"""

    A = MonitoringStation('idA', 'measureA', 'A', (0, 0), (0, 1), 'riverA', 'townA')
    B = MonitoringStation('idB', 'measureB', 'B', (1, 1), (0, 1), 'riverB', 'townB')
    C = MonitoringStation('idC', 'measureC', 'C', (-2, -2), (0, 1), 'riverC', 'townC')

    stations = [A, B, C]
    p = (0, 0)
    r = 2000

    result = geo.stations_within_radius(stations, p, r)
    assert A in result
    assert B in result
    assert C not in result