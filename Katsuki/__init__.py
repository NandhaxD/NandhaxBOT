
import os 
import time
import sys
import logging
import config

from pyrogram import Client
from pymongo import MongoClient, errors as Mongoerrors

StartTime = time.time()

MODULE = []



class CustomFilter(logging.Filter):
    def filter(self, record):
        if "Loaded Plugins from" in record.msg:  # replace the message
            record.msg = record.msg.replace("Loaded Plugins from", "Plugins loaded from")
        return True

logging.getLogger("pyrogram").setLevel(logging.DEBUG)  # set logging level
handler = logging.FileHandler("logs.txt")  # create file handler
handler.setFormatter(logging.Formatter("%(asctime)s [%(name)s]: %(message)s"))  # use default formatter
handler.addFilter(CustomFilter())  # add custom filter to handler



# PYROGRAM USER CLIENT 
app = Client(name="katsuki", session_string=config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki"),
logging_level=logging.DEBUG, handlers=[handler])


#PYROGRAM BOT CLIENT
bot = Client(name="KatsukiBot", bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki"),
logging_level=logging.DEBUG, handlers=[handler])

# PYMONGO DATABASE
DB = MongoClient(config.DB_URL)

try:
   DB.server_info()
except Mongoerrors.ConnectionFailure:
     print("Connection failure, INVALID MONGO DB URL!, DOWN!")
     sys.exit()


DATABASE = DB.MAIN


# CLASS FOR INFO GETTING
class INFO:
    """ USER CLIENT INFO """
    async def app():
         info = await app.get_me()
         return info
    """ BOT CLIENT INFO """
    async def bot():
         info = await bot.get_me()
         return info
    
 