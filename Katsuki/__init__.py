
import os 
import time
import sys
import logging
from pyrogram import Client
from pymongo import MongoClient 

StartTime = time.time()

# LOGGING INFO
FORMAT = "[Katsuki]: %(message)s"
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)




# SETUP VARIABLE IN HOSTING WEBSITE ENVIRONMENT 

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("TOKEN")
SESSION = os.getenv("SESSION") 

# PYROGRAM USER CLIENT 
katsuki = Client(name="Katsuki", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Katsuki/"),)


#PYROGRAM BOT CLIENT
app = Client(name="KatsukiBot", api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Katsuki/"),)

# PYMONGO DATABASE
DB_URL = "mongodb+srv://nandhasigma:iqKZ5OnIBVcpZde2@cluster0.gt47zau.mongodb.net/?retryWrites=true&w=majority"
DB = MongoClient(DB_URL)

try:
   DB..server_info()
except ConnectionFailure:
     logging.info("Connection failure, Invalid MONGOB URL!, DOWN!")
     sys.exit()


DATABASE = DB.MAIN




