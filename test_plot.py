import datetime
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels

def test_plot_water_levels_execution():
    """Test that the plotting function handles data correctly."""
    
    #Create a dummy station
    station_id = "test-id"
    measure_id = "test-measure"
    label = "Test Station"
    coord = (52.2053, 0.1218)
    typical_range = (0.2, 0.8)
    river = "River Cam"
    town = "Cambridge"
    
    test_station = MonitoringStation(station_id, measure_id, label, coord, 
    typical_range, river, town)

    #Create dummy time and level data
    now = datetime.datetime.now()
    dates = [now - datetime.timedelta(hours=i) for i in range(10)]
    levels = [0.1, 0.2, 0.4, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.8]

  
   
   
    try:
        assert len(dates) == len(levels) # Ensure that the lengths of dates and levels match
        assert test_station.name == "Test Station" # Check that the station name is correct
        
        plot_water_levels(test_station, dates, levels)
    except Exception as e:
        assert False, f"plot_water_levels raised an exception: {e}"

def test_station_consistency_for_plot():
    """Test that the consistency check used in plotting works."""
    s = MonitoringStation("1", "1", "Stat", (0,0), (0.5, 0.2), "R", "T")
    # This range is inconsistent (high < low)
    assert s.typical_range_consistent() == False # Check that the consistency check correctly identifies inconsistent ranges