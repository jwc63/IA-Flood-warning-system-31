import numpy as np
from floodsystem.station import MonitoringStation

from Task2G import risk_level

def test_risk_level():
    """Tests the risk_level function"""

    A = MonitoringStation('idA', 'measureA', 'A', (0, 0), (0, 1), 'riverA', 'townA')
    B = MonitoringStation('idB', 'measureB', 'B', (1, 1), (0, 1), 'riverB', 'townB')
    C = MonitoringStation('idC', 'measureC', 'C', (-2, -2), (0, 1), 'riverC', 'townC')

    A.relative_water_level = 1.7
    B.relative_water_level = 1.3
    C.relative_water_level = 0.5

    stations = [A, B, C]

    for station in stations:
        result = risk_level(station, 1.5, 1.2, 0.8)
        if station == A:
            assert result == "Severe"
        elif station == B:
            assert result == "High"
        elif station == C:
            assert result == "Low"