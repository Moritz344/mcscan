import rich
from rich.panel import Panel
from rich.console import Console
from termcolor import cprint,colored
from rich.box import *
import rich.layout



def get_data(players_on,players_max,players_list_on,status,version,motd,mods_list,port,eula_blocked,host,plugins_list):
    console = Console()

    players_list_on = ",".join(players_list_on)
    
    status_color = "[green]"
    if status:
        status = "Online"
        status_color = "[green]"
    else:
        status = "Offline"
        status_color = "[red]"

    motd = motd.split()
    motd = "  ".join(motd)
    

    mods_list= ",".join(mods_list)

    plugins_list = ",".join(plugins_list)

    if mods_list == "":
        mods_list = "N/A"
    if not eula_blocked:
        eula_blocked = "No"
    else:
        eula_blocked = "Yes"

    if plugins_list == "":
        plugins_list = "N/A"

    p0 = rich.panel.Panel(f"[magenta]Status:      [/magenta]    {status_color}{status}",box=rich.box.ROUNDED,highlight=True,)
    p1 = rich.panel.Panel(f"[magenta]Host:        [/magenta]    {host}",box=rich.box.ROUNDED,highlight=True,)
    p2 = rich.panel.Panel(f"[magenta]Port:        [/magenta]    {status_color}{port}",box=rich.box.ROUNDED,highlight=True,)
    p3 = rich.panel.Panel(f"[magenta]MOTD:        [/magenta]    [blue]{motd}",box=rich.box.ROUNDED,highlight=True,)
    p4 = rich.panel.Panel(f"[magenta]Version:     [/magenta]    [blue]{version}",box=rich.box.ROUNDED,highlight=True,)
    p5 = rich.panel.Panel(f"[magenta]Players:     [/magenta]    {players_on}/{players_max}", box=rich.box.ROUNDED,highlight=True)

    p6 = rich.panel.Panel(f"[magenta]Mods:        [/magenta]    {mods_list}", box=rich.box.ROUNDED,highlight=True)
    p7 = rich.panel.Panel(f"[magenta]Plugins:     [/magenta]    {plugins_list}", box=rich.box.ROUNDED,highlight=True)
    p8 = rich.panel.Panel(f"[magenta]EULA Blocked:[/magenta]    {eula_blocked}/{eula_blocked}", box=rich.box.ROUNDED,highlight=True)

    p9 = rich.panel.Panel(f"[magenta]Player list: [/magenta]    {players_list_on}", box=rich.box.ROUNDED,highlight=True)
    console.clear()
    console.print(p0,p1,p2,p3,p4,p5,p6,p7,p8)


