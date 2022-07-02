import config
import os 
import logging
from pyrogram import Client

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)



Kasuki = Client(session_string=config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH, name="Katsuki")
