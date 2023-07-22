from simple_term_menu import TerminalMenu
from time import sleep
from modules.weather import *

try: 
    def run_weather():
        run_weather.options = [
            "🌨  Weather Forecast From Station",
            None,
            "🗺  Weather Forecast From Geo Coordinates",
            None,
            "📢 Get Alerts by Area Code",
            None,
            "Back to Main Menu"
        ]
        run_weather.terminal_menu = TerminalMenu(
            run_weather.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
        )
        run_weather.menu_entry_index = run_weather.terminal_menu.show() / 2
        if run_weather.menu_entry_index == 0:
            weather_forecast_from_station()
            
        if run_weather.menu_entry_index == 1:
            weather_forecast_from_geo()

        if run_weather.menu_entry_index == 2:
            alerts_from_area_code()
        

    run_weather()

except KeyboardInterrupt:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    # brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    # run_again()
