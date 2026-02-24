import datetime

# Using the import style from your Task 1D
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    # 1. Build list of stations
    print("Step 1: Building station list...")
    stations = build_station_list()

    # 2. Update water levels 
    # This step downloads a lot of data. It might take 30-60 seconds.
    print("Step 2: Updating water levels (fetching real-time data)...")
    update_water_levels(stations)

    # 3. Identify the top 5 stations at risk using your Task 2C logic
    print("Step 3: Finding the 5 stations with highest relative levels...")
    top_5_at_risk = stations_highest_rel_level(stations, 5)

    # 4. Fetch history and plot for these stations
    dt = 10  # Look back 10 days
    print(f"Step 4: Fetching 10-day history for the top {len(top_5_at_risk)} stations...")

    for entry in top_5_at_risk:
        # Based on your flood.py, stations_highest_rel_level returns (station, level)
        station = entry[0]
        
        try:
            # Fetch historical data
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt)
            )

            # Check if we got valid data back to plot
            if dates and levels:
                print(f"Generating plot for: {station.name}")
                plot_water_levels(station, dates, levels)
            else:
                print(f"No historical data available for: {station.name}")
        
        except Exception as e:
            # This prevents the "JSONDecodeError" from stopping the whole program
            print(f"Could not fetch data for {station.name} (Server Error). Skipping...")

if __name__ == "__main__":
    print("*** Task 2E: Water Level Plots ***")
    run()