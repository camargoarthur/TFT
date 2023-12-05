import requests

summonerName="Jagu4tz"
api_key="RGAPI-60f408b8-7ebc-4fef-a366-2cd6bad75e9c"
api_url=("https://br1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"+summonerName+"?api_key="+api_key)

resp = requests.get(api_url)
player_info = resp.json()

puuid = player_info['puuid']
print(puuid)