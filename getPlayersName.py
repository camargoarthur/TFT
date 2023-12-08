import requests
import pymongo
from getPlayerInfo import api_key  

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['tft']
collection = db['matches']

base_url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/'


documents_to_review = collection.find({"$or": [{"reviewDados": {"$exists": False}}, {"reviewDados": False}]})

for document in documents_to_review:
    if document.get('reviewDados', False):
        print(f"Document {document['_id']} already reviewed. Skipping...")
        continue

    participants = document['metadata']['participants']
    game_names = {}

    for participant in participants:
        url = f"{base_url}{participant}?api_key={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            player_info = response.json()
            game_names[participant] = player_info.get("gameName")
        else:
            print(f"Failed to fetch data for participant {participant}. Status code: {response.status_code}")

   
    collection.update_one(
        {"_id": document["_id"]},
        {"$set": {
            "info.participants": [
                { 
                    **participant_data,
                    "gameName": game_names.get(participant_data['puuid'], 'Unknown')
                }
                for participant_data in document['info']['participants']
            ],
            "reviewDados": True
        }}
    )
    print(f"Document updated: {document['_id']}")
