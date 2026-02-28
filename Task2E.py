import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    
    print("Step 1: Building station list...")
    stations = build_station_list() #list of all stations 

    
    
    print("Step 2: Updating water levels (fetching real-time data)...")
    update_water_levels(stations) #updates the water levels for all stations in the list

    
    print("Step 3: Finding the 5 stations with highest relative levels...")
    top_5_at_risk = stations_highest_rel_level(stations, 5) #returns list of top 5 stations with highest water levels

    
    dt = 10  # Look back 10 days
    print(f"Step 4: Fetching 10-day history for the top {len(top_5_at_risk)} stations...")# Loop through the top 5 stations and fetch their historical water level data for the past 10 days

    for entry in top_5_at_risk:

        station = entry[0]
        
        try:
            #fetches historical water level data for the last ten days (returns two lists: one with the dates and another with the corresponding water levels)
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt)
            )

           #if there is valid data then it plots
            if dates and levels:
                print(f"Generating plot for: {station.name}")
                plot_water_levels(station, dates, levels)
            else:
                print(f"No historical data available for: {station.name}")
        
        except Exception as e: #if exception it prints error message and move sonto to the next station this prevents it crashing the entire programme
           
            print(f"Could not fetch data for {station.name} (Server Error). Skipping...")

if __name__ == "__main__": #only runs if this file is run directly
    print("*** Task 2E: Water Level Plots ***")
    run()