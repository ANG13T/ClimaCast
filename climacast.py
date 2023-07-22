# from modules.weather import *

# get_forecast_from_lat_lon(39.7456, -97.0892)


try:
    """
    Imports the main menu with all its functions
    """

    from modules.menu import menu

except KeyboardInterrupt:
    os.system("clear")
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")