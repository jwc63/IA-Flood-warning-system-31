from floodsystem import geo
from floodsystem import stationdata

Cambridge_city_centre = (52.2053, 0.1218)

stations = stationdata.build_station_list()

distances = geo.stations_by_distance(stations, Cambridge_city_centre)

closest_stations = []
for station, distance in distances[:10]:    
    closest_stations.append((station.name, station.town, distance))
furthest_stations = []
for station, distance in distances[10:]:    
    furthest_stations.append((station.name, station.town, distance))

print("The 10 closest stations are:" + closest_stations)
print("The 10 furthest stations are:" + furthest_stations)

##(station name, town, distance)