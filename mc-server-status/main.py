import requests
import rich
from handling_requests import *

base_url = "https://api.mcstatus.io/v2"

host = get_server_info(base_url)

class Main(object):
    def __init__(self,host):
        self.host = host

        print(self.host)
        
Main(host)


def cli_entry_point():
    pass


