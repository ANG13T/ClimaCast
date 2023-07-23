from services.noaa import *
from rich.console import Console
from rich.table import Table


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
        result = get_point_lat_lon(lat,lon)

        if result != None:
            print_geo_data(lat, lon, result)
            get_forecast(result['forecast'])
       

def alerts_from_area_code():
    return

def print_data_row(title, value):
    value = "• [bold]{}:[/] [cyan]{}[/]".format(title, value)
    console = Console()
    console.print(value)

def print_geo_data(lat, lon, geo_data):
    table_title = "\n [bold blue underline]Information for ({}, {})[/]".format(lat, lon)
    location_info = geo_data['relativeLocation']['properties']
    distance = "{}m".format(location_info["distance"]["value"])
    bearing = "{}º".format(location_info["bearing"]["value"])
    console = Console()
    console.print(table_title + "\n")
    print_data_row("🏢 Office", derive_value_from_api(geo_data["forecastOffice"]))
    print_data_row("📍 GPS", "({}, {})".format(lat, lon))
    print_data_row("🗺  County", derive_value_from_api(geo_data["county"]))
    print_data_row("📡 Radar Station", derive_value_from_api(geo_data["radarStation"]))
    print_data_row("🕙 Time Zone", derive_value_from_api(geo_data["timeZone"]))
    print_data_row("🌧  Forecast Zone", derive_value_from_api(geo_data["forecastZone"]))
    print_data_row("🏙  City", location_info["city"])
    print_data_row("🌆 State", location_info["state"])
    print_data_row("🚶 Distance", distance)
    print_data_row("📐 Bearing", bearing)


def get_forecast(url):
    table = Table(title="Forecast Data")
    table.add_column("Name", style="cyan", no_wrap=True, justify="center")
    table.add_column("Start Time", style="cyan", no_wrap=True, justify="center")
    table.add_column("End Time", style="cyan", no_wrap=True, justify="center")
    table.add_column("Time of Day", style="magenta", justify="center")
    table.add_column("Temperature", style="magenta", justify="center")
    table.add_column("Dewpoint", style="magenta", justify="center")
    table.add_column("Relative Humidity", style="magenta", justify="center")
    table.add_column("Windspeed", style="magenta", justify="center")
    table.add_column("Notes", style="magenta", justify="center")

    result = get_value_from_url(url)

    if "properties" in result:
        observations = result['properties']['periods']
        for ob in observations:
            if ob["isDaytime"] == True:
                time_of_day = "Daytime"
            else:
                time_of_day = "Nighttime"

            dew_point = str(ob["dewpoint"]["value"]) + "ºC"
            rel_humidity = str(ob["relativeHumidity"]["value"]) + "%"
            temp = str(ob['temperature']) + ob["temperatureUnit"]
            wind = ob["windSpeed"] + " " + ob["windDirection"]

            table.add_row(
                ob["name"],
                ob["startTime"],
                ob["endTime"],
                time_of_day,
                temp,
                dew_point,
                rel_humidity,
                wind,
                ob["detailedForecast"]
            )
            
        console = Console()
        console.print(table)

def print_row(row_id, row_value):
    print('{}: {}'.format(row_id, row_value))

def print_forecast_data(json):
    get_forecast(json['forecast'], derive_value_from_api(json['@id']), derive_value_from_api(json['forecastOffice']))
