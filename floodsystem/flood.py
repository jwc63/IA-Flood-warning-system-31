from floodsystem.utils import sorted_by_key
def stations_level_over_threshold(stations, tol):      
    """returns list of stations with relative level over threshold tolerance"""

    over_threshold = []

    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() > tol:
            over_threshold.append((station, station.relative_water_level()))
    
    return sorted_by_key(over_threshold, 1, reverse = True)
 

def stations_highest_rel_level(stations, N):
    """returns list of N stations with highest relative water level"""

    stations_with_rel_level = []

    for station in stations:
        if station.relative_water_level() != None:
            stations_with_rel_level.append((station, station.relative_water_level()))
    
    rel_level_ordered = sorted_by_key(stations_with_rel_level, 1, reverse = True)

    return rel_level_ordered[:N]