# Com o sumoner name localizar o puuid do jogador
# A api_key precisa ser atualizada a cada 24 horas

import requests

summonerName="Jagu4tz"
api_key="RGAPI-13521b4d-3fe6-415d-855c-93f5ef47e48b"
api_url=("https://br1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"+summonerName+"?api_key="+api_key)

resp = requests.get(api_url)
player_info = resp.json()

puuid = player_info['puuid']
print(puuid)