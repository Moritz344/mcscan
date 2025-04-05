import rich
from rich.panel import Panel
from rich.console import Console
from termcolor import cprint,colored
from rich.box import *
import rich.layout



def get_data(players_on,players_max,players_list_on,status,version):
    console = Console()

    players_list_on = ",".join(players_list_on)
    
    status_color = "[green]"
    if status:
        status = "Online"
        status_color = "[green]"
    else:
        status = "Offline"
        status_color = "[red]"

    p0 = rich.panel.Panel(f"[magenta]Status:      [/magenta]    {status_color}{status}",box=rich.box.ROUNDED,highlight=True,)
    p1 = rich.panel.Panel(f"[magenta]Version:     [/magenta]    [blue]{version}",box=rich.box.ROUNDED,highlight=True,)
    p2 = rich.panel.Panel(f"[magenta]Players:     [/magenta]    {players_on}/{players_max}", box=rich.box.ROUNDED,highlight=True)
    p3 = rich.panel.Panel(f"[magenta]Player list: [/magenta]    {players_list_on}", box=rich.box.ROUNDED,highlight=True)

    console.print(p0,p1,p2,p3)


