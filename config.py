

import os, sys


""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", True)


if ENV:    
   API_ID = os.getenv("API_ID")
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   SESSION = os.getenv("SESSION")
   GROUP_ID = os.getenv("GROUP_ID")
   DB_URL = os.getenv("DB_URL")
   HANDLER = os.getenv("HANDLER")
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
   KATSUKI = None # your alive photo
   HANDLER = None # example ".,?".split(",")
   DB_URL = None # get from mongodb.com


""" DEFAULT VARIABLES """

if not HANDLER:
     HANDLER = ["~", ".","!","?","@","$"]



""" REQUIRED VARIABLES """

SOURCE = "https://github.com/nandhaxd/katsuki"
NAME = "Katsuki"


