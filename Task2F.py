import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    #Build and update station data
    print("Step 1: Building station list...")
    stations = build_station_list()
    
    #fetches real-time data from the EA server and updates each station
    print("Step 2: Updating water levels (this may take a moment)...")
    update_water_levels(stations)

    #Get the top 5 stations with highest relative levels
    print("Step 3: Finding top 5 at-risk stations...")
    top_5 = stations_highest_rel_level(stations, 5) 

    #Fetch history and plot with polynomial fit
    dt = 2      #fetches 2 days of history for trend line
    degree = 4  # Polynomial degree
    
    print(f"Step 4: Fetching 2-day history and plotting with degree {degree} fit...")

    for entry in top_5:
        # Unpack the tuple (station, relative_level)
        station = entry[0]
        
        try:
            # Fetch historical data
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt)
            )

            # Check if we have data to plot
            if dates and levels:
                print(f"Generating plot with fit for: {station.name}")
                plot_water_level_with_fit(station, dates, levels, degree)
            else:
                print(f"No historical data available for: {station.name}")
        
        except Exception as e:
            # Catches potential server errors to keep the script running
            print(f"Skipping {station.name} due to a server error.")

if __name__ == "__main__":
    print("*** Task 2F: Water Level Plots with Polynomial Fit ***")
    run()