import requests
import json

def get_server_info(base) -> str:

    response = requests.get(f"{base}/status/java/play.thirdplacemc.net")
    if response.status_code == 200:
        data = response.json()
        host = data["host"]
        players_on = data["players"]["online"]
        players_max = data["players"]["max"]

        player_list_on: list = []
        status: bool = data["online"]
        max_number: int = 20

        for player in range(0,players_on):
            name = data["players"]["list"][player]["name_clean"]
            if player < max_number: # damit bei großen servern nicht '3000' Spieler Namen angezeigt werden
                player_list_on.append(name)

            
        
        print(player_list_on)

    else:
        print("Error")

    
    return host
