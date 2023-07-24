import requests
import os
from dotenv import load_dotenv
from rich.table import Table
from rich.console import Console

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

def get_value(value, object):
    if value in object:
        return object[value]
    else:
        return "No Value"

def print_vis_passes(name, passes):
    passes = passes["passes"]
    table_title = "Visual Passes for {}".format(name)
    table = Table(title=table_title)
    console = Console()
    table.add_column("Start Azimuth", style="cyan",  justify="center")
    table.add_column("Start Elevation", style="cyan",  justify="center")
    table.add_column("Start UTC", style="cyan", justify="center")
    table.add_column("Max Azimuth", style="cyan",  justify="center")
    table.add_column("Max Elevation", style="cyan",  justify="center")
    table.add_column("Max UTC", style="cyan",  justify="center")
    table.add_column("End Azimuth", style="cyan",  justify="center")
    table.add_column("End Elevation", style="cyan",  justify="center")
    table.add_column("End UTC", style="cyan",  justify="center")
    table.add_column("Max Magnitude", style="cyan",  justify="center")
    table.add_column("Duration", style="cyan",  justify="center")

    for pos in passes:
        start_az = str(get_value('startAz', pos)) +  " " + get_value('startAzCompass', pos)
        start_el = str(get_value('startEl', pos)) + "º"
        start_utc = str(get_value('startUTC', pos)) + "UTC"
        max_az = str(get_value('maxAz', pos)) +  " " + get_value('maxAzCompass', pos)
        max_el = str(get_value('maxEl', pos)) + "º"
        max_utc = str(get_value('maxUTC', pos)) + "UTC"
        end_az = str(get_value('endAz', pos)) +  " " + get_value('endAzCompass', pos)
        end_el = str(get_value('endEl', pos)) + "º"
        end_utc = str(get_value('endUTC', pos)) + "UTC"
        mag = str(get_value("mag", pos))
        duration = str(get_value("duration", pos)) + "sec"

        table.add_row(
            start_az,
            start_el,
            start_utc,
            max_az,
            max_el,
            max_utc,
            end_az,
            end_el,
            end_utc,
            mag,
            duration
        )

    console.print(table)

def print_radio_passes(name, passes):
    passes = passes["passes"]
    table_title = "Radio Passes for {}".format(name)
    table = Table(title=table_title)
    console = Console()
    table.add_column("Start Azimuth", style="cyan",  justify="center")
    table.add_column("Start UTC", style="cyan", justify="center")
    table.add_column("Max Azimuth", style="cyan",  justify="center")
    table.add_column("Max Elevation", style="cyan",  justify="center")
    table.add_column("Max UTC", style="cyan",  justify="center")
    table.add_column("End Azimuth", style="cyan",  justify="center")
    table.add_column("End Elevation", style="cyan",  justify="center")
    table.add_column("End UTC", style="cyan",  justify="center")

    for pos in passes:
        start_az = str(get_value('startAz', pos)) +  " " + get_value('startAzCompass', pos)
        start_utc = str(get_value('startUTC', pos)) + "UTC"
        max_az = str(get_value('maxAz', pos)) +  " " + get_value('maxAzCompass', pos)
        max_el = str(get_value('maxEl', pos)) + "º"
        max_utc = str(get_value('maxUTC', pos)) + "UTC"
        end_az = str(get_value('endAz', pos)) +  " " + get_value('endAzCompass', pos)
        end_el = str(get_value('endEl', pos)) + "º"
        end_utc = str(get_value('endUTC', pos)) + "UTC"

        table.add_row(
            start_az,
            start_utc,
            max_az,
            max_el,
            max_utc,
            end_az,
            end_el,
            end_utc
        )

    console.print(table)

def print_positions(name, positions):
    positions = positions["positions"]
    table_title = "Positions for {}".format(name)
    table = Table(title=table_title)
    console = Console()
    table.add_column("GPS", style="cyan",  justify="center")
    table.add_column("Azimuth", style="cyan", justify="center")
    table.add_column("Elevation", style="cyan",  justify="center")
    table.add_column("Right Ascension", style="cyan",  justify="center")
    table.add_column("Declination", style="cyan",  justify="center")
    table.add_column("Timestamp", style="cyan",  justify="center")

    for pos in positions:
        gps = "(" + str(pos['satlatitude']) + ", " + str(pos['satlongitude']) + ")"
        az = str(pos['azimuth']) + "º"
        elevation = str(pos['elevation']) + "º"
        ra = str(pos['ra']) + "º"
        dec = str(pos['dec']) + "º"
        timestamp = str(pos['timestamp']) + "sec"

        table.add_row(
            gps,
            az,
            elevation,
            ra,
            dec,
            timestamp
        )

    console.print(table)