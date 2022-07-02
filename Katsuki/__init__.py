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


API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 

bot = Client("KatsukiBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))
Katsuki = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="Katsuki")
