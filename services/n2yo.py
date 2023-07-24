import requests
import os
from dotenv import load_dotenv

api_url = "https://api.n2yo.com/rest/v1/satellite"

def get_api_key():
    load_dotenv()
    return os.getenv('N2YO_API')

def get_radio_pass(norad_id, lat, lng, alt, days, elevation):
    format_api = '/radiopasses/{}/{}/{}/{}/{}/{}'.format(norad_id, lat, lng, alt, days, elevation)
    url = api_url + format_api + "&apiKey=" + get_api_key()
    response = requests.get(url)
    return response.json()

def get_visual_pass(norad_id, lat, lng, alt, days, vis):
    format_api = '/visualpasses/{}/{}/{}/{}/{}/{}'.format(norad_id, lat, lng, alt, days, vis)
    url = api_url + format_api + "&apiKey=" + get_api_key()
    response = requests.get(url)
    return response.json()

def get_positions(norad_id, lat, lng, alt, seconds):
    format_api = '/positions/{}/{}/{}/{}/{}'.format(norad_id, lat, lng, alt, seconds)
    url = api_url + format_api + "&apiKey=" + get_api_key()
    response = requests.get(url)
    return response.json()

def get_point_lat_lon(lat, long):
    if check_coordinates(lat, long):
        return True
    else: 
        print("ERROR: Use Valid GPS Coordinate")
        return None

def check_coordinates(lat, long):
    try: 
        lat = float(lat)
        long = float(long)
        return abs(lat) <= 90 and abs(long) <= 180
    except:
        return False
    
def verify_values(values):
    result = True
    for val in values:
        try:
            float_value = float(val)
            if isinstance(float_value, float) == False:
                result = None
        except ValueError:
            print("ERROR: Use Valid Satellite Values")
            return None
    return result