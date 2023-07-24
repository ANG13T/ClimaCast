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