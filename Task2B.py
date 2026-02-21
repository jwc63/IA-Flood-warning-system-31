from floodsystem import flood
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()

    stationdata.update_water_levels(stations)

    stations_over_threshold = flood.stations_level_over_threshold(stations, 0.8)

    for station, level in stations_over_threshold:
        print(station.name, level)

if __name__ == "__main__":
    run()