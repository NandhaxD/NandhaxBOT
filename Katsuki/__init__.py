
import os 
import time
import sys
import logging
import config

from pyrogram import Client
from pymongo import MongoClient, errors 

StartTime = time.time()

# LOGGING INFO
FORMAT = "[Katsuki Client]: %(message)s"
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)



# PYROGRAM USER CLIENT 
app = Client(name="katsuki", session_string=config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki/"),)


#PYROGRAM BOT CLIENT

bot = Client(name="KatsukiBot", bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki/"),)

# PYMONGO DATABASE
DB = MongoClient(config.DB_URL)

try:
   DB.server_info()
except errors.ConnectionFailure:
     logging.info("Connection failure, Invalid MONGOB URL!, DOWN!")
     sys.exit()


DATABASE = DB.MAIN


# INFO FUNC
class INFO:
    async def app():
         info = await app.get_me()
         return info

    async def bot():
         info = await bot.get_me()
         return info
 