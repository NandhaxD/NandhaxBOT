"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



import os, sys, requests, pyrogram, typing



""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", True)



if ENV:    
   API_ID = os.getenv("API_ID", 13257951)
   API_HASH = os.getenv("API_HASH", "d8ea642aedb736d40035bc05f0cfd477")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   SESSION = os.getenv('SESSION')
   GROUP_ID = os.getenv("GROUP_ID", -1001717881477)
   OWNER_ID = int(os.getenv('OWNER_ID', 5696053228))
   GROUP_LINK = os.getenv('GROUP_LINK', "nandhasupport.t.me")
   DB_URL = os.getenv("DB_URL", "mongodb+srv://nandhaxd:hIatwh7wpArjRPX3@cluster0.80igexg.mongodb.net")
   LANG_CODE = os.getenv('LANG_CODE', 'en')
         
else:
   API_ID = 12345 #int() method | get from my.telegram.org
   API_HASH = "abcde" #str() method | get from my.telegram.org
   BOT_TOKEN = "token" #str() method | get via @botfather
   SESSION = "" #string session pyrogram
   DB_URL = "" # get from mongodb.com
   GROUP_LINK = "t.me/nandhasupport"
   OWNER_ID = 5696053228 # fill ur user id
   LANG_CODE = 'en'



### BOT INFO ###
bot_info = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getme').json()['result']
BOT_ID = bot_info['id']
BOT_USERNAME = bot_info['username']
BOT_NAME = NAME = bot_info['first_name']



PREFIXES = ["~", ".","!","?","@","$"] 

SOURCE = "https://github.com/nandhaxd/nandhaxbot"


def command(cmd: typing.Union[str, list]):
    commands = []
    if isinstance(cmd, str):
        commands.extend([cmd, f'@{BOT_USERNAME}'])
    elif isinstance(cmd, list):
        for comm in cmd:
            commands.extend([comm, f'@{BOT_USERNAME}'])
    return pyrogram.filters.command(commands, prefixes=PREFIXES)
