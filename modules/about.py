from rich.console import Console
from simple_term_menu import TerminalMenu

def about():
    console = Console()
    console.print("\n[bold underline cyan]About ClimaCast[/]\n")
    console.print("ClimaCast is a command-line tool written with Python that provides meteorology reports and forecasts, satellite pass predictions, communications decoding, and imagery analysis on NOAA satellites.")
    console.print("\n[bold underline cyan]ClimaCast Purpose[/]\n")
    console.print("The purpose of ClimaCast is to provide a suite of tools that make satellite NOAA data accessible to researchers, developers, and enthusiasts. The suite contains most of the tools necessary to extract and audit remote sensing information from the NOAA satellite constellation.")
    console.print("\n[bold underline cyan]ClimaCast Utilities[/]\n")
    console.print("🌦  [bold]Weather Forecasts and Alerts[/]\n")
    console.print("Get up-to-date weather forecasts, data, amd alerts from NOAA satellites. You can choose to get information via GPS coordinates, station ID, or area code")
    console.print("\n🛰  [bold]Pass Predictor[/]\n")
    console.print("Predict for radio or visual satellite passes of all NOAA satellites by inputting your GPS coordinates")
    console.print("\n📡  [bold]APT Image Decoder[/]\n")
    console.print("Decode NOAA satellite images by inputting audio MP3 files of satellite transmissions.")
    console.print("\n🌎  [bold]Meterological Image Analysis[/]\n")
    console.print("Retrieve meterological images from the Sentinel-2 data collection for remote sensing analysis.")
    console.print("\n[bold underline cyan]About the Developer[/]\n")
    console.print("ClimaCast was created by Angelina Tsuboi (G4LXY). To get in touch with me, you can reach out via the following methods:\n")
    console.print("[bold]Website:[/] angelinatsuboi.com")
    console.print("[bold]Instagram:[/] @angelina_tsuboi")
    console.print("[bold]Twitter:[/] @AngelinaTsuboi")
    console.print("[bold]GitHub:[/] @ANG13T")
    console.print("\n[bold underline cyan]Contributing and Support[/]\n")
    console.print("All contributions to this tool are welcome. Please refer the contribution guideline on ClimaCast's GitHub repository to submit a pull request.")
    console.print("To support my work and future projects, please consider sponsoring me on GitHub:")
    console.print("https://github.com/sponsors/ANG13T")
    console.print("\n[bold]ClimaCast GitHub Repo:[/]")
    console.print("https://github.com/ANG13T/ClimaCast")

    about.options = [
            "Back to Main Menu"
        ]
    about.terminal_menu = TerminalMenu(
        about.options,
        title="",
        menu_cursor="❯ ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("fg_blue", "underline", "bold"),
    )

    about.terminal_menu.show()