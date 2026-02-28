import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """
    Displays a plot of the water level data against time for a station,
    including lines for typical low and high levels.
    """
    plt.plot(dates, levels, label="Water Level")

    if station.typical_range_consistent():
        low_val = station.typical_range[0]
        high_val = station.typical_range[1]
        plt.axhline(y=low_val, color='g', linestyle='--', label='Typical Low')
        plt.axhline(y=high_val, color='r', linestyle='--', label='Typical High')

    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station: {station.name}")
    plt.legend()
    plt.tight_layout()
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from .analysis import polyfit 

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots water level data and a polynomial fit."""
    
    # Plot the raw data (the jagged blue line)
    plt.plot(dates, levels, '.', label="Raw Data")
    
    # Calculate the polynomial fit
    poly, d0 = polyfit(dates, levels, p)
    
    #Create a smooth line for the polynomial
    x = mdates.date2num(dates)
    x_smooth = np.linspace(x[0], x[-1], 100)
    plt.plot(x_smooth, poly(x_smooth - d0), label=f"Polynomial fit (degree {p})")
    
    # Add typical range lines if consistent
    if station.typical_range_consistent():
        plt.axhline(y=station.typical_range[0], color='g', linestyle='--', label='Typical Low')
        plt.axhline(y=station.typical_range[1], color='r', linestyle='--', label='Typical High')
        
    # Formatting
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station: {station.name}")
    plt.legend()
    plt.tight_layout()
    plt.show()   