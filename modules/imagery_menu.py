from simple_term_menu import TerminalMenu
from time import sleep
from modules.imagery import *
from rich.console import Console
import os
from modules.menu import banner, menu_print, rerun

console = Console()

try: 
    def run_imagery():
        run_imagery.options = [
            "🎨 Retrieve JPEG Image",
            None,
            "📡 Retrieve Raster Data",
            None,
            "Back to Main Menu"
        ]
        run_imagery.terminal_menu = TerminalMenu(
            run_imagery.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
        )
        run_imagery.menu_entry_index = run_imagery.terminal_menu.show() / 2
        if run_imagery.menu_entry_index == 0:
            fetch_image()
            
        if run_imagery.menu_entry_index == 1:
            retrieve_raster_data()
        

    run_imagery()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting ClimaCast [/cyan][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    banner()
    menu_print()
    print(f"\n[bold][red] INVALID COMMAND [/red][/bold]")
    rerun()
