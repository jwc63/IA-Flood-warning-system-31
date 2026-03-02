import numpy as np
import datetime
import matplotlib.dates as mdates
from floodsystem.analysis import polyfit

def test_polyfit():
    """Test the polynomial fitting function."""
    
    # Create dummy data
    now = datetime.datetime.now()
    dates = [now - datetime.timedelta(days=i) for i in range(10)]
    levels = [0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0.0, 0.1, 0.2]
    
    p = 4  # Degree 4
    
    #Run polyfit
    poly, d0 = polyfit(dates, levels, p)
    
    
    # Check that poly is a numpy polynomial object
    assert isinstance(poly, np.poly1d)
    
    # Check that the degree is correct
    assert poly.order == p
    
    # Check that d0 is the float representation of the latest date
    assert d0 == mdates.date2num(dates[0])
    


    sample_val = poly(0)
    assert isinstance(sample_val, float)