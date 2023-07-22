from modules import *
from simple_term_menu import TerminalMenu
try:
    #main_menu()

    def menu():
        """
        Main Menu, Select from all four options
        """
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
        menu.menu_entry_index = terminal_menu.show()

        if menu.options[menu.menu_entry_index] == "Directory Scanner":
            # import modules.scanner
            print("hi")

        if menu.options[menu.menu_entry_index] == "Subdomain Scanner":
            #import modules.subdomain_scanner
            print("hi")

        if menu.options[menu.menu_entry_index] == "Wordlists":
            # modify_wordlist()
            # run_again()
            print("hi")

        if menu.options[menu.menu_entry_index] == "About And Warnings":
            # about()
            # run_again()
            print("hi")

    menu()

except KeyboardInterrupt:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    # time.sleep(2)

except TypeError:
    # os.system("clear")
    # brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    # run_again()