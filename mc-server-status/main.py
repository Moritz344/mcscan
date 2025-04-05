import requests
import rich
from handling_requests import *
from format_data import get_data

run = True

class Main(object):
    def __init__(self):
        self.base_url = "https://api.mcstatus.io/v2"


    def update(self):
        try:
            server_name: input = input("Server: ")
            players_on,players_max,players_list_on,status,version = get_server_info(self.base_url,server_name)
            get_data(players_on,players_max,players_list_on,status,version)
        except Exception as e:
            print("No data found for this server.")



        




def cli_entry_point():
    app = Main()
    while run:
        app.update()

cli_entry_point()

