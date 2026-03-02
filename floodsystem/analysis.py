import matplotlib.dates as mdates
import numpy as np

def polyfit(dates, levels, p):
    """Given water level time history, finds a polynomial fit of degree p."""
    
    # Convert dates to numerical values (days since Year 1)
    x = mdates.date2num(dates)
    y = levels
    
    # Shift the x-axis so the latest data point is 0
    # This prevents numerical errors with large date numbers
    d0 = x[0]
    x_shifted = x - d0
    
    # Find the polynomial coefficients
    p_coeffs = np.polyfit(x_shifted, y, p)
    
    # Convert coefficients to a polynomial object
    poly = np.poly1d(p_coeffs)
    
    return poly, d0