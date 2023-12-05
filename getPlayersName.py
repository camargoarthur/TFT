#Pegar o puuid dos participantes da partida, chamar a API pra pegar o name e adicionar a collection do mongo no campo "participants.playerName"
from pymongo import MongoClient
from getPlayerInfo import api_key
