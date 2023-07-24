from simple_term_menu import TerminalMenu
from time import sleep
from modules.passes import *
from rich.console import Console

console = Console()

try: 
    def run_pass():
        run_pass.options = [
            "🔭 Retrieve Visual Passes",
            None,
            "📡 Retrieve Radio Passes",
            None,
            "🛰  Retrieve Positioning",
            None,
            "Back to Main Menu"
        ]
        run_pass.terminal_menu = TerminalMenu(
            run_pass.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
        )
        run_pass.menu_entry_index = run_pass.terminal_menu.show() / 2
        if run_pass.menu_entry_index == 0:
            retrieve_visual_passes()
            
        if run_pass.menu_entry_index == 1:
            retrieve_radio_passes()

        if run_pass.menu_entry_index == 2:
            retrieve_TLE()
        

    run_pass()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting ClimaCast [/cyan][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    console.print("\n[bold][red] INVALID COMMAND [/red][/bold]")
    # run_again()
