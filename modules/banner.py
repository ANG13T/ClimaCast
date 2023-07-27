import os
from rich.console import Console

console = Console()

def banner():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, './assets/banner.txt')
    f = open(file_name, 'r')
    file_contents = f.read()
    console.print("\n [cyan]" + file_contents + "[/]")
    f.close()
    console.print("[blue bold]    Created by Angelina Tsuboi (angelinatsuboi.com)[/]")
    console.print("              [blue underline]github.com/ANG13T/ClimaCast[/] \n")

def menu_print():
    print("══════════════════ ClimaCast Options ══════════════════")
           