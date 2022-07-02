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

SESSION = config.SESSION
API_ID = config.API_ID
API_HASH = config.API_HASH

Kasuki = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="Katsuki")
