import requests


player_name = 'floppa_b'
player_id = None
game_id = "csgo"
api_header = {"Authorization": "Bearer " + '67bae541-fce2-4093-b777-f0a363edcc75',
                           "content-type": "application/json"}



player_id_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname=" + player_name + "&game=CSGO",headers=api_header)
print(player_id_request.text)
cu=player_id_request.cookies
player_id_data = player_id_request.json()
player_id = player_id_data["player_id"]
print(player_id)

player_history_request = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/history?game=csgo", headers=api_header, cookies=cu)
print(player_history_request.status_code)
print(player_history_request.text)