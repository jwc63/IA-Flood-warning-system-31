from floodsystem import station
from floodsystem import stationdata

stations = stationdata.build_station_list()

inconsistent_stations = station.inconsistent_typical_range_stations(stations)

inconsistent_station_names = []
for s in inconsistent_stations:
    inconsistent_station_names.append(s.name)

print(sorted(inconsistent_station_names))