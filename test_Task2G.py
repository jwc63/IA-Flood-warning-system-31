import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit 

from Task2G import increasing_stations, risk_level

def test_increasing_stations():