from services.noaa import *

def get_forecast_from_lat_lon(lat, long):
    result = get_point_lat_lon(lat,long)
    print(result)