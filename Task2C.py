from floodsystem import flood
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()

    stationdata.update_water_levels(stations)

    stations_over_threshold = flood.stations_highest_rel_level(stations, 10)

    for station, level in stations_over_threshold:
        print(station.name, level)

if __name__ == "__main__":
    run()