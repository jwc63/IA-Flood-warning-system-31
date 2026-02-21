from floodsystem import flood
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    """Tests stations_level_over_threshold"""

    A = MonitoringStation('idA', 'measureA', 'A', (0, 0), (0, 1), 'riverA', 'townA')
    B = MonitoringStation('idB', 'measureB', 'B', (1, 1), (0, 1), 'riverB', 'townB')
    C = MonitoringStation('idC', 'measureC', 'C', (-2, -2), (0, 1), 'riverC', 'townC')

    A._relative_water_level = 0.9
    B._relative_water_level = 0.7
    C._relative_water_level = None

    stations = [A, B, C]
    tol = 0.8

    result = flood.stations_level_over_threshold(stations, tol)
    assert result[0][0] == A
    assert result[0][1] == 0.9

def test_stations_highest_rel_level():
    """Tests stations_highest_rel_level"""

    A = MonitoringStation('idA', 'measureA', 'A', (0, 0), (0, 1), 'riverA', 'townA')
    B = MonitoringStation('idB', 'measureB', 'B', (1, 1), (0, 1), 'riverB', 'townB')
    C = MonitoringStation('idC', 'measureC', 'C', (-2, -2), (0, 1), 'riverC', 'townC')
    D = MonitoringStation('idD', 'measureD', 'D', (-2, -2), (0, 1), 'riverD', 'townD')

    A._relative_water_level = 0.9
    B._relative_water_level = 0.7
    C._relative_water_level = None
    D._relative_water_level = 0.8
    stations = [A, B, C, D]
    N = 2

    result = flood.stations_highest_rel_level(stations, N)
    assert result[0][0] == A
    assert result[0][1] == 0.9
    assert result[1][0] == D
    assert result[1][1] == 0.8