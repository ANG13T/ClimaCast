from modules import *
from time import sleep
from simple_term_menu import TerminalMenu
from modules.rerun import rerun
from modules.about import about
from modules.banner import *

try:
    banner()
    menu_print()

    def menu():
        menu.options = [
            "🌦  Weather Forecasts and Alerts",
            None,
            "🛰  Pass Predictor",
            None,
            "📡  APT Image Decoder",
            None,
            "🌎  Meterological Image Analysis",
            None,
            "ℹ️  About and Usage",
            None,
            "Exit ClimaCast",
        ]

        terminal_menu = TerminalMenu(
            menu.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
            skip_empty_entries=True
        )
        menu.menu_entry_index = terminal_menu.show()  / 2

        if menu.menu_entry_index == 0:
            import modules.weather_menu
            rerun()

        if menu.menu_entry_index == 1:
            import modules.passes_menu
            rerun()

        if menu.menu_entry_index == 2:
            import modules.decoder_menu
            rerun()

        if menu.menu_entry_index == 3:
            # about()
            rerun()

        if menu.menu_entry_index == 4:
            about()
            rerun()
        
        if menu.menu_entry_index == 5:
            print("[bold][blue] Exiting...[/blue][/bold]")
            sleep(1)

    menu()

except KeyboardInterrupt:
    print("\n")
    print("[bold][blue] Exiting...[/blue][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    # brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    # run_again()