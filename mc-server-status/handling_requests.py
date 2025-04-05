import requests
import json


def get_server_info(base,server) -> str:
    response = requests.get(f"{base}/status/java/{server}")
    if response.status_code == 200:
        data = response.json()
        host = data["host"]
        players_on = data["players"]["online"]
        players_max: max = data["players"]["max"]
        version = data["version"]["name_clean"]
        player_list_on: list = []
        status: bool = data["online"]
        # maximale nummer die ich bekomme von der api
        max_number: int = 12

        if players_on < 100:
            for index in range(0,players_on ):
                if index < max_number:
                    name = data["players"]["list"][index]["name_clean"]
                    player_list_on.append(name)
                else:
                    continue


        return players_on,players_max,player_list_on,status,version

        

    else:
        print(response.status_code)

    
