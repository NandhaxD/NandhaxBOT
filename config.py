"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import os, sys, Katsuki


""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", True)


if ENV:    
   API_ID = os.getenv("API_ID")
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   SESSION = os.getenv("SESSION")
   GROUP_ID = os.getenv("GROUP_ID")
   DB_URL = os.getenv("DB_URL")
   LIST_OF_VARIABLE = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION", "GROUP_ID", "DB_URL"]   
   for var in LIST_OF_VARIABLE:
      if not os.getenv(var):
           sys.exit()
           print(f"THE {var} ENVIRONMENT VARIABLE IS MISSING.")
else:
   API_ID = None #int() method | get from my.telegram.org
   API_HASH = None #str() method | get from my.telegram.org
   BOT_TOKEN = None #str() method | get via @botfather
   SESSION = None #str() method | use replit or bots to get your Pyro session 
   GROUP_ID = None #int() menthod | your group id
   DB_URL = None # get from mongodb.com


""" DEFAULT VARIABLES """


HANDLER = ["~", ".","!","?","@","$"]   
NAME = Katsuki.INFO.app()['name']
BOT_USERNAME = Katsuki.INFO.bot()['username']



""" REQUIRED VARIABLES """

SOURCE = "https://github.com/nandhaxd/katsuki"



