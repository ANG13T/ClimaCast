from simple_term_menu import TerminalMenu
from time import sleep
from modules.decoder import *
from rich.console import Console

console = Console()

try: 
    def run_decoder():
        run_decoder.options = [
            "🛰 Decode NOAA Recording",
            None,
            "📡 Resample NOAA Recording",
            None,
            "Back to Main Menu"
        ]
        run_decoder.terminal_menu = TerminalMenu(
            run_decoder.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
        )
        run_decoder.menu_entry_index = run_decoder.terminal_menu.show() / 2
        if run_decoder.menu_entry_index == 0:
            run_decode_file()
            
        if run_decoder.menu_entry_index == 1:
            run_resample_file()
        

    run_decoder()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting ClimaCast [/cyan][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    console.print("\n[bold][red] INVALID COMMAND [/red][/bold]")
    # run_again()
