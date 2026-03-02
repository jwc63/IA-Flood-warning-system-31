from floodsystem.stationdata import build_station_list
from Task1D import stations_by_river  

def rivers_by_station_number(stations, N):
    river_to_stations = stations_by_river(stations) 

    
    river_counts = [(river, len(stations)) for river, stations in river_to_stations.items()]
    #sorts the tuples into a list
    
    river_counts.sort(key=lambda x: x[1], reverse=True)

    
    if N <= len(river_counts): #checks we have atleast 9 rivers in the list
        cutoff = river_counts[N-1][1] #only rivers with at least as many station as the nth river are included
        result = []
        result = [rc for rc in river_counts if rc[1] >= cutoff] #if it has less than cutoff its not included
    else:
        result = river_counts #if theres are less rivers than N it does nothing and just gives all the rivers and their stations

    return result

def run():
    stations = build_station_list() 
    N = 9
    top_rivers = rivers_by_station_number(stations, N)
    print(top_rivers)

if __name__ == "__main__":
    run()
