from floodsystem import geo
from floodsystem import stationdata

Cambridge_city_centre = (52.2053, 0.1218)

stations = stationdata.build_station_list()

radius = geo.stations_within_radius(stations, Cambridge_city_centre, 10)

stations_in_radius = []

for station in radius:    
    stations_in_radius.append((station.name))

print(sorted(stations_in_radius))