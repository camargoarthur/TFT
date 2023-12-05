import pandas as pd
from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['tft']
collection = db['matches']

#Importar dados
dados = list(collection.find())
df = pd.DataFrame(dados)
client.close()