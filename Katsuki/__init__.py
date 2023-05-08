
import os 
import time
import logging
from pyrogram import Client
from pymongo import MongoClient 


StartTime = time.time()


FORMAT = "[Katsuki]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)




#setup variable in hosting website environment 

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION") 

katsuki = Client(name="Katsuki", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Katsuki"),)

DB_URL = "mongodb+srv://nandhasigma:iqKZ5OnIBVcpZde2@cluster0.gt47zau.mongodb.net/?retryWrites=true&w=majority"
DB = MongoClient(DB_URL)
DATABASE = DB.MAIN

