
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



import os 
import time
import sys
import logging
import config

from pyrogram import Client
from pymongo import MongoClient, errors as Mongoerrors

StartTime = time.time()

MODULE = []



# LOGGING INFO

FORMAT = f"[{config.NAME}] %(message)s"
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)




# PYROGRAM USER CLIENT 
app = Client(name="katsuki", session_string=config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki"))

#PYROGRAM BOT CLIENT
bot = Client(name="KatsukiBot", bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="Katsuki"))

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
    
 