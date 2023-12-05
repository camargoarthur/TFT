#Pegar os dados da partida baseado no puuid
import datetime
import requests
from pymongo import MongoClient
from getPlayerInfo import puuid
from getPlayerInfo import api_key

# Conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['tft']
collection = db['matches']

api_url = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api_key}"

resp = requests.get(api_url)
matches_id = resp.json()

base_url = 'https://americas.api.riotgames.com/tft/match/v1/matches/'

# Calcular a data de ontem
data_ontem = datetime.datetime.utcnow() - datetime.timedelta(days=1)
data_ontem_str = data_ontem.strftime('%Y-%m-%d')

for match_id in matches_id:
    match_url = f"{base_url}{match_id}?api_key={api_key}"
    match_resp = requests.get(match_url)
    
    if match_resp.status_code == 200:
        match_data = match_resp.json()
        
        match_timestamp = match_data['info']['game_datetime']
        date = datetime.datetime.utcfromtimestamp(match_timestamp / 1000)
        formatted_date = date.strftime('%Y-%m-%d')
        
        match_data['dtpartida'] = formatted_date

        
        if formatted_date == data_ontem_str:
            collection.insert_one(match_data)
    else:
        print(f"Erro ao buscar dados para o match ID {match_id}. Código de status: {match_resp.status_code}")

client.close()
