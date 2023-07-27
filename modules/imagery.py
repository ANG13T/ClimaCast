from pystac_client import Client
from shapely.geometry import Point
import requests
from simple_term_menu import TerminalMenu
from rich.console import Console

api_url = "https://earth-search.aws.element84.com/v1"

# Sentinel-2, Level 2A, Cloud Optimized GeoTiffs (COGs)
collection = "sentinel-2-l2a" 

console = Console()

def fetch_image(output, lat, lng):
    
    client = Client.open(api_url)
    point = Point(lat, lng)


    search = client.search(
        collections=[collection],
        intersects=point,
        max_items=10,
    )

    items = search.item_collection()
    assets = items[0].assets

    image_url = assets["thumbnail"].href

    img_data = requests.get(image_url).content
    with open(output, 'wb') as handler:
        handler.write(img_data)
        console.print("\n [green bold]SAVED SATELLITE JPG IMAGE TO {}[/]".format(output))

def download_tiff(output, lat, lng):
    client = Client.open(api_url)
    point = Point(lat, lng)


    search = client.search(
        collections=[collection],
        intersects=point,
        max_items=10,
    )

    items = search.item_collection()
    assets = items[0].assets

    download_tiff.options = []
    
    for key, asset in assets.items():
        if asset.title[len(asset.title) - 4:].lower() == "tiff":
            download_tiff.options.append(asset.title)

        print(asset.title[len(asset.title) - 4:].lower())
        print(asset)
    
    download_tiff.terminal_menu = TerminalMenu(
        download_tiff.options,
        title="",
        menu_cursor=" ❯ ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("fg_cyan", "underline", "bold"),
    )

    download_tiff.menu_entry_index = download_tiff.terminal_menu.show()
    # print out output path and metadata


def retrieve_jpeg_image():
    output  = console.input("Enter [bold blue]Output Path[/]: ")
    result = False

    while result != True:
        lat = console.input("Enter [bold blue]Latitude[/]: ")
        lon = console.input("Enter [bold blue]Longitude[/]: ")

        if check_file(output, ".jpg") and check_coordinates(lat, lon):
            result = True
            if len(output) == 0:
                output = "../output/output.jpg"

            fetch_image(output, lat, lon)
    

def retrieve_raster_data():
    output  = console.input("Enter [bold blue]Output Path[/]: ")
    result = False

    while result != True:
        lat = console.input("Enter [bold blue]Latitude[/]: ")
        lon = console.input("Enter [bold blue]Longitude[/]: ")

        if check_file(output, ".tiff") and check_coordinates(lat, lon):
            result = True
            if len(output) == 0:
                output = "../output/output.tiff"

            download_tiff(output, lat, lon)

def check_coordinates(lat, long):
    try: 
        lat = float(lat)
        long = float(long)
        return abs(lat) <= 90 and abs(long) <= 180
    except:
        console.print("[red]INVALID GPS COORDINATES[/]")
        return False
    
def check_file(name, ext):
    str_len = len(ext)
    name_ext = name[len(name) - str_len:].lower()
    if name_ext == ext:
        return True
    else:
        console.print("[red]INVALID FILE EXTENSION[/]")
        return False