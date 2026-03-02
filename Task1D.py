from floodsystem.stationdata import build_station_list  # imports the function build_station_list from stationdata.py, this function creates a list of all the monitoring stations
from floodsystem.geo import stations_by_distance, stations_within_radius  #imports the function stations_by_distance and stations_within_radius from geo.py. These functionscalculate the distance between stations and a given point, and find stations within a certain radius respectively.

#this gives us the name of the rivers which have atleast one station associated with them.
def rivers_with_station(stations): 
    river_names = set() 
    for station in stations:  
        if station.river: 
            river_names.add(station.river) 
    return river_names

#gives a list of stations which are associated with each river
def stations_by_river(stations):
    rivers_to_stations = {} 
    for station in stations:
        river = station.river 
        if river:
            if river not in rivers_to_stations: 
                rivers_to_stations[river] = [] 
            rivers_to_stations[river].append(station) 
    return rivers_to_stations



def run():
    stations = build_station_list() 

    #Rivers with at least one monitoring station
    rivers = rivers_with_station(stations) 
    sorted_rivers = sorted(rivers) 
    print(f"{len(sorted_rivers)} rivers. First 10: {sorted_rivers[:10]}") 

    # Stations by river
    river_to_stations = stations_by_river(stations) 

    def print_stations_for_river(river_name): 
        station_list = river_to_stations.get(river_name, []) #allows to retrieve the list of stations for the specified river name from the river_to_stations dictionary. If the river name is not found, it returns an empty list
        station_names = sorted([station.name for station in station_list]) #creates a sorted list of station names for the stations associated with the specified river
        print(f"\nStations on {river_name}:") 
        print(station_names)

    print_stations_for_river("River Aire")
    print_stations_for_river("River Cam")
    print_stations_for_river("River Thames")

if __name__ == "__main__": 
    run()
