from modules import *
from time import sleep
from simple_term_menu import TerminalMenu
from modules.rerun import rerun
from modules.about import about

try:
    #main_menu()

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
            "🛠  Settings",
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
            # modify_wordlist()
            # run_again()
            print("hi")

        if menu.menu_entry_index == 3:
            # about()
            # run_again()
            print("hi")
        
        if menu.menu_entry_index == 4:
            # about()
            # run_again()
            print("hi")

        if menu.menu_entry_index == 5:
            about()
        
        if menu.menu_entry_index == 6:
            print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
            sleep(1)

    menu()

except KeyboardInterrupt:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    # brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    # run_again()