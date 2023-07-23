from rich.console import Console
from simple_term_menu import TerminalMenu

def about():
    console = Console()
    console.print("\n[bold underline cyan]About ClimaCast [/]")
    console.print("ClimaCast is a command-line tool written with Python that provides meteorology reports and forecasts, satellite pass predictions, communications decoding, and imagery analysis on NOAA satellites")
    console.print("\n[bold underline cyan]ClimaCast Purpose [/]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")
    console.print("\n[bold underline cyan]ClimaCast Utilities [/]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")
    console.print("\n[bold underline cyan]About the Developer [/]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")
    console.print("\n[bold underline cyan]Contributing and Support [/]")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")

    about.options = [
            "Back to Main Menu"
        ]
    about.terminal_menu = TerminalMenu(
        about.options,
        title="",
        menu_cursor=" ❯ ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("fg_cyan", "underline", "bold"),
    )

    about.terminal_menu.show()