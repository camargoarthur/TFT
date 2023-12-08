import pandas as pd
from pymongo import MongoClient
from getPlayerInfo import puuid

# Configurações DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['tft']
collection = db['matches']

# Importar dados
dados = list(collection.find())
df = pd.DataFrame(dados)
client.close()

# Dados tabela matchs
match_id = df['metadata'].apply(lambda x: x.get('match_id'))

def extract_participant_data(participants, target_puuid):
    data = {
        'Match_ID': [],
        'Level': [],
        'Placement': [],
        'Players_Eliminated': [],
        'Last_Round': [],
        'Total_Damage_to_Players': []
    }
    for participant in participants:
        if participant.get('puuid') == target_puuid:
            data['Level'].append(participant.get('level'))
            data['Placement'].append(participant.get('placement'))
            data['Players_Eliminated'].append(participant.get('players_eliminated'))
            data['Last_Round'].append(participant.get('last_round'))
            data['Total_Damage_to_Players'].append(participant.get('total_damage_to_players'))
    return pd.DataFrame(data)
