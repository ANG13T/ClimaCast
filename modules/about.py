from rich.console import Console

def about():
    console = Console()
    console.print("\n [bold underline] About ClimaCast [\]")
    console.print("ClimaCast is a command-line tool written with Python that provides meteorology reports and forecasts, satellite pass predictions, communications decoding, and imagery analysis on NOAA satellites")
    console.print("\n [bold underline] ClimaCast Purpose [\]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")
    console.print("\n [bold underline] About the Developer [\]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")

def back_menu():
    return