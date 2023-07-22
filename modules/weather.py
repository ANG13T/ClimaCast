from services.noaa import *
from rich.console import Console


def weather_forecast_from_station():
    console = Console()
    value = console.input("Enter [bold blue]Station ID[/]: ")
    print(value)

def weather_forecast_from_geo():
    console = Console()
    result = None
    while result == None:
        lat = console.input("Enter [bold blue]Latitude[/]: ")
        lon = console.input("Enter [bold blue]Longitude[/]: ")
        print(lon)
        result = get_point_lat_lon(lat,lon)
        # print(result)
    # print_forecast_data(result)

def alerts_from_area_code():
    return


def get_forecast(url):
    result = get_value_from_url(url)
    print_row('generatedAt', result['properties']['generatedAt'])
    print_row('updateTime', result['properties']['updateTime'])
    print_row('elevation', result['properties']['elevation'])
    print(result['properties']['coordinates'])
    observations = result['properties']['periods']
    for ob in observations:
        print_observation(ob)

def print_observation(observation):
    print_row('temperature', observation['temperature'])

def print_row(row_id, row_value):
    print('{}: {}'.format(row_id, row_value))

def print_forecast_data(json):
    print('GPS: ({})'.format(derive_value_from_api(json['@id'])))
    print('OFFICE: {}'.format(derive_value_from_api(json['forecastOffice'])))
    get_forecast(json['forecast'])
    # Forecast
    # Observation Stations
