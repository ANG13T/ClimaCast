# from modules.weather import *
import os
from dotenv import load_dotenv
from rich.console import Console

# get_forecast_from_lat_lon(39.7456, -97.0892)
console = Console()


try:
    """
    Imports the main menu with all its functions
    """
    def import_env():
        load_dotenv()
        N2YO_Key = os.getenv('N2YO_API')
        if N2YO_Key == "API_KEY_HERE":
            console.print("[bold blue]Put N2YO API Key in .env file[/]")
            return False
        else:
            return True

    if import_env():
        from modules.menu import menu

except KeyboardInterrupt:
    os.system("clear")
    console.print("\n")
    console.print("[bold][blue] Exiting...[/blue][/bold]")