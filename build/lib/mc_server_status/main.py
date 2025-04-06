import requests
import rich
from mc_server_status.handling_requests import *
from mc_server_status.format_data import get_data
from termcolor import colored
import sys

run = True



class Main(object):
    def __init__(self):
        self.base_url = "https://api.mcstatus.io/v2"


    def update(self):
        try:
            server_name: input = input(str(colored("Server: ","blue",attrs=["blink"])))
            players_on,players_max,players_list_on,status,version,motd,mods_list, port,eula_blocked,host,plugins_list = get_server_info(self.base_url,server_name)
            get_data(players_on,players_max,players_list_on,status,version,motd,mods_list, port,eula_blocked,host,plugins_list)
        except Exception as e:
            print(colored("No server with this name found.","red",attrs=["bold"]))
        except KeyboardInterrupt:
            print(colored("Goodbye!","green"))
            sys.exit(0)


def cli_entry_point():
    app = Main()
    while run:
        app.update()
if __name__ == "__main__":
    cli_entry_point()

