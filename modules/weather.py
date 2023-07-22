from services.noaa import *

def get_forecast_from_lat_lon(lat, long):
    result = get_point_lat_lon(lat,long)
    print(result)
    print_forecast_data(result)

def print_forecast_data(json):
    print('GPS: ({})'.format(derive_value_from_api(json['@id'])))
    print('OFFICE: {}'.format(derive_value_from_api(json['forecastOffice'])))
    # Forecast
    # Observation Stations
    