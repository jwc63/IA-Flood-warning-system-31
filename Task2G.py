import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit 

def increasing_stations(stations, tol):
    # Calculate the polynomial fit
    poly, d0 = polyfit(dates, levels, p)

    #calculate derivative
    poly_deriv = np.polyder(poly)

    increasing = []
    for station in stations:
        if station.relative_water_level() != None and poly_deriv(d0) > tol:
            increasing.append(station)
    return increasing


def risk_level(station, sev_tol, high_tol, mod_tol):
    """returns list of stations at risk of flooding"""

    if station.relative_water_level() == None:
        return "Unknown"
    elif station.relative_water_level() < mod_tol:
        return "Low"
    elif station.relative_water_level() < high_tol:
        return "Moderate"
    elif station.relative_water_level() < sev_tol:
        return "High"
    else:
        return "Severe"


def run():
    stations = build_station_list()
    update_water_levels(stations)

    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []

    for station in stations:
        risk = risk_level(station, 1.2, 0.1, 0.05)
        increasing = increasing_stations(stations, 0.1)
        if risk == "Severe" or ((risk == "High" or risk == "Moderate") and station in increasing):
            severe_risk.append(station.town)
        elif risk == "High" or (risk == "Moderate" and station in increasing):
            high_risk.append(station.town)
        elif risk == "Moderate":
            moderate_risk.append(station.town)
        elif risk == "Low":
            low_risk.append(station.town)


    print("Towns at risk of flooding:")
    print("Severe Risk:")
    print(severe_risk)
    print("High Risk:")
    print(high_risk)
    print("Moderate Risk:")
    print(moderate_risk)
    print("Low Risk:")
    print(low_risk)


if __name__ == "__main__":
    run()