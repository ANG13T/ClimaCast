from services.noaa import *
from rich.console import Console
from rich.table import Table


def weather_forecast_from_station():
    console = Console()
    value = console.input("Enter [bold blue]Station ID[/]: ")
    result = get_station_metadata(value)

    if result != None:
        observations = get_station_observations(value)["features"]
        print_station_metadata(value, result)
        print_observations(value, observations)
    else:
        console.print("[red]INVALID STATION ID[/]")


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
            # TODO: show nearby stations
       

def alerts_from_area_code():
    console = Console()
    value = console.input("Enter [bold blue]Area Code[/]: ")
    result = get_alerts_by_area(value)

    if result != None: 
        print_area_metadata(value, result)
        print_alerts(value, result)
    else:
        console.print("[red]INVALID AREA CODE[/]")


def print_data_row(title, value):
    value = "• [bold]{}:[/] [cyan]{}[/]".format(title, value)
    console = Console()
    console.print(value)

def print_area_metadata(id, data):
    table_title = "\n [bold blue underline]Information for Area {}[/]".format(id)
    console = Console()
    console.print(table_title + "\n")
    print_data_row("📡 Identifier", id)
    print_data_row("🌧  Notes", data["title"])
    print_data_row("🕙 Time Stamp", data["updated"])

def print_alerts(id, alerts):
    alerts = alerts["features"]
    table_title = "Alerts for {}".format(id)
    table = Table(title=table_title)
    table.add_column("Area", style="cyan",  justify="center")
    table.add_column("Sent Timestamp", style="cyan", justify="center")
    table.add_column("Effective Timestamp", style="cyan",  justify="center")
    table.add_column("Status", style="cyan",  justify="center")
    table.add_column("Type", style="cyan",  justify="center")
    table.add_column("Category", style="cyan",  justify="center")
    table.add_column("Severity", style="cyan",  justify="center")
    table.add_column("Certainty", style="cyan",  justify="center")
    table.add_column("Urgency", style="cyan",  justify="center")
    table.add_column("Event", style="cyan",  justify="center")
    table.add_column("Sender", style="cyan",  justify="center")
    table.add_column("Headline", style="cyan",  justify="center")
    table.add_column("Instruction", style="cyan",  justify="center")
    
    for al in alerts:
        al = al["properties"]
        table.add_row(
            al["areaDesc"],
            al["sent"],
            al["effective"],
            al["status"],
            al["messageType"],
            al["category"],
            al["severity"],
            al["certainty"],
            al["urgency"],
            al["event"],
            al["senderName"],
            al["headline"],
            al["instruction"]
        )

    console = Console()
    console.print(table)


def print_station_metadata(id, data):
    table_title = "\n [bold blue underline]Information for Station {}[/]".format(id)
    console = Console()
    console.print(table_title + "\n")
    lat = data["geometry"]["coordinates"][0]
    lon = data["geometry"]["coordinates"][1]
    props = data["properties"]
    elevation = str(props["elevation"]["value"]) + "m"
    print_data_row("🏢 Identifier", id)
    print_data_row("📡 Name", props["name"])
    print_data_row("🌧  Type", props["@type"][3:])
    print_data_row("📍 GPS", "({}, {})".format(lat, lon))
    print_data_row("🏔  Elevation", elevation)
    print_data_row("🕙 Time Zone", props["timeZone"])
    print_data_row("🏙  County", derive_value_from_api(props["county"]))

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

def check_no_reading(value):
    if "None" in value:
        return "No Reading"
    else:
        return value

def print_observations(id, observations):
    table_title = "Observations for Station {}".format(id)
    table = Table(title=table_title)
    table.add_column("Timestamp", style="cyan", no_wrap=True, justify="center")
    table.add_column("Temperature", style="cyan", no_wrap=True, justify="center")
    table.add_column("Dewpoint", style="cyan", no_wrap=True, justify="center")
    table.add_column("Wind Speed", style="magenta", justify="center")
    table.add_column("Wind Gust", style="magenta", justify="center")
    table.add_column("Baro Pressure", style="magenta", justify="center")
    table.add_column("Sea Level Pressure", style="magenta", justify="center")
    table.add_column("Visibility", style="magenta", justify="center")
    table.add_column("Relative Humidity", style="magenta", justify="center")
    table.add_column("Heat Index", style="magenta", justify="center")

    for ob in observations:
        ob = ob["properties"]
        temp = str(ob['temperature']['value']) + "ºC"
        dewpoint = str(ob['dewpoint']['value']) + "ºC"
        windspeed = str(ob['windSpeed']['value']) + "km/hr "
        if ob['windDirection']["value"] != None:
            windspeed += str(ob['windDirection']["value"]) + "º"

        if ob['windGust']["value"] != None:
            gust = str(ob['windGust']["value"]) + "km/hr"
        else:
            gust = "0 km/hr"

        baro = str(ob['barometricPressure']["value"]) + "Pa"

        if ob['seaLevelPressure']["value"] != None:
            sea = str(ob['seaLevelPressure']["value"]) + "Pa"
        else:
            sea = "No Reading"

        if ob['visibility']["value"] != None:
            vis = str(ob['visibility']["value"]) + "m"
        else:
            vis = "No Reading"

        rel_hum = str(ob['relativeHumidity']["value"]) + "%"
        heat_index = str(ob['heatIndex']['value']) + "ºC"

        table.add_row(
            ob["timestamp"],
            check_no_reading(temp),
            check_no_reading(dewpoint),
            check_no_reading(windspeed),
            check_no_reading(gust),
            check_no_reading(baro),
            check_no_reading(sea),
            check_no_reading(vis),
            check_no_reading(rel_hum),
            check_no_reading(heat_index)
        )

    console = Console()
    console.print(table)
        

def get_forecast(url):
    table = Table(title="Forecast Data")
    table.add_column("Name", style="cyan", no_wrap=True, justify="center")
    table.add_column("Start Time", style="cyan", no_wrap=True, justify="center")
    table.add_column("End Time", style="cyan", no_wrap=True, justify="center")
    table.add_column("Time of Day", style="magenta", justify="center")
    table.add_column("Temperature", style="magenta", justify="center")
    table.add_column("Dewpoint", style="magenta", justify="center")
    table.add_column("Relative Humidity", style="magenta", justify="center")
    table.add_column("Wind Speed", style="magenta", justify="center")
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