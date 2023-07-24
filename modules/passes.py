from services.n2yo import *
from rich.console import Console
from simple_term_menu import TerminalMenu

class Satellite:
    def __init__(self, name, id):
        self.name = name
        self.norad_id = id


def retrieve_radio_passes():
    console = Console()
    selected = select_NOAA_sat()

    if selected != None:
        result = False

        while result != True:
            lat = console.input("Enter [bold blue]Latitude[/]: ")
            lon = console.input("Enter [bold blue]Longitude[/]: ")
            alt = console.input("Enter [bold blue]Altitude[/]: ")
            days = console.input("Enter [bold blue]Days[/]: ")
            elevation = console.input("Enter [bold blue]Elevation[/]: ")
            result = verify_values([alt, days, elevation])
            geo_res = check_coordinates(lat, lon)
            if geo_res == None:
                result = None

            if result == True:
                passes = get_radio_pass(selected.norad_id, lat, lon, alt, days, elevation)
                print_radio_passes(selected.name, passes)


def retrieve_visual_passes():
    console = Console()
    selected = select_NOAA_sat()

    if selected != None:
        result = False

        while result != True:
            lat = console.input("Enter [bold blue]Latitude[/]: ")
            lon = console.input("Enter [bold blue]Longitude[/]: ")
            alt = console.input("Enter [bold blue]Altitude[/]: ")
            days = console.input("Enter [bold blue]Days[/]: ")
            vis = console.input("Enter [bold blue]Min Visibility[/]: ")
            result = verify_values([alt, days, vis])
            geo_res = check_coordinates(lat, lon)
            if geo_res == None:
                result = None

            if result == True:
                passes = get_visual_pass(selected.norad_id, lat, lon, alt, days, vis)
                print_vis_passes(selected.name, passes)


def retrieve_positions():
    console = Console()
    selected = select_NOAA_sat()

    if selected != None:
        result = False

        while result != True:
            lat = console.input("Enter [bold blue]Latitude[/]: ")
            lon = console.input("Enter [bold blue]Longitude[/]: ")
            alt = console.input("Enter [bold blue]Altitude[/]: ")
            sec = console.input("Enter [bold blue]Min Seconds[/]: ")
            result = verify_values([alt, sec])
            geo_res = check_coordinates(lat, lon)
            if geo_res == None:
                result = None

            if result == True:
                print(get_positions(selected.norad_id, lat, lon, alt, sec))


def select_NOAA_sat():
    select_NOAA_sat.options = []

    noaa_sats = [
        Satellite("NOAA-21 (JPSS-2)", 54234),
        Satellite("NOAA 20 (JPSS 1)", 43013),
        Satellite("DSCOVR", 40390),
        Satellite("SUOMI NPP", 37849),
        Satellite("NOAA 19", 33591),
        Satellite("NOAA 18", 28654),
        Satellite("NOAA 17", 27453),
        Satellite("NOAA 16", 26536),
        Satellite("NOAA 15", 25338),
        Satellite("NOAA 14", 23455),
        Satellite("NOAA 13", 22739),
        Satellite("NOAA 12", 21263),
        Satellite("NOAA 11", 19531),
        Satellite("NOAA 10", 16969),
        Satellite("NOAA 9", 15427),
        Satellite("NOAA 8", 13923),
        Satellite("NOAA 7", 12553),
        Satellite("NOAA 6", 11416),
        Satellite("TIROS N", 11060),
        Satellite("NOAA 5", 9057),
        Satellite("NOAA 4", 7529),
        Satellite("NOAA 3", 6920),
        Satellite("NOAA 2 (ITOS-D)", 6235),
        Satellite("NOAA 1", 4793),
    ]

    for sat in noaa_sats:
        select_NOAA_sat.options.append(sat.name + " (" + str(sat.norad_id) + ")")

    select_NOAA_sat.options.append(None)
    select_NOAA_sat.options.append("Back to Main Menu")

    select_NOAA_sat.terminal_menu = TerminalMenu(
        select_NOAA_sat.options,
        title="",
        menu_cursor=" ❯ ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("fg_cyan", "underline", "bold"),
    )

    select_NOAA_sat.menu_entry_index = select_NOAA_sat.terminal_menu.show() 

    if select_NOAA_sat.menu_entry_index == 25 or select_NOAA_sat.menu_entry_index == 24:
        return None
    else:
        return noaa_sats[select_NOAA_sat.menu_entry_index]
    
