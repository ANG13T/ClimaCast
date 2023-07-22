import requests

api_url = "https://api.weather.gov"

def get_point_lat_lon(lat, long):
    if check_coordinates(lat, long):
        format_api = '/points/{},{}'.format(lat, long)
        response = requests.get(api_url + format_api)
        return response.json()['properties']
    else: 
        print("ERROR: Use Valid GPS Coordinate")
        return None

def get_station_metadata(station_id):
    format_api = '/stations/{}'.format(station_id)
    response = requests.get(api_url + format_api)
    print(response.json())

def get_station_observations(station_id):
    format_api = '/stations/{}/observations'.format(station_id)
    response = requests.get(api_url + format_api)
    print(response.json())

def get_stations_from_point(lat, long):
    if check_coordinates(lat, long):
        format_api = '/points/{},{}/stations'.format(lat, long)
        response = requests.get(api_url + format_api)
        print(response.json())
    else: 
        print("ERROR: Use Valid GPS Coordinate")

def get_alerts_by_area(area):
    format_api = '/alerts/active/area/{}'.format(area)
    response = requests.get(api_url + format_api)
    print(response.json())

def get_value_from_url(url):
    response = requests.get(url)
    return response.json()

def check_coordinates(lat, long):
    return abs(lat) <= 90 and abs(long) <= 180

def derive_value_from_api(api_url):
    return api_url.split("/")[-1]