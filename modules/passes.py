import os
from dotenv import load_dotenv
from simple_term_menu import TerminalMenu

class Satellite:
    def __init__(self, name, id):
        self.name = name
        self.nora_id = id


def retrieve_radio_passes():
    selected = select_NOAA_sat()

    if selected != None:
        return

def retrieve_visual_passes():
    selected = select_NOAA_sat()

    if selected != None:
        return

def retrieve_TLE():
    selected = select_NOAA_sat()

    if selected != None:
        return

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
        select_NOAA_sat.options.append(sat.name + " (" + str(sat.nora_id) + ")")

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