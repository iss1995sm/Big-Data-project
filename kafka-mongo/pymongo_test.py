
import pymongo
from pymongo import MongoClient
import json
from datetime import datetime
import time

# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb+srv://ivansimo:{pass}@cluster0.aoi5b.mongodb.net/gettingStarted?retryWrites=true&w=majority')

db = client.Nosql_Anuncios

collection = db.Nosql_Clients

db = client['noSQL_Client']

collection = db['noSQL_Collection']

inicID = 'objectIdentifier'
objectIdentifier = '007'

collection.insert_one({"_id": 'objectIdentifier', "SISTEMA INICIADO": True})
