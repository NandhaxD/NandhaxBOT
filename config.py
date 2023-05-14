

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
   HANDLER = ["~", ".","!","?","@","$"]
   LIST_OF_VARIABLE = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION", "GROUP_ID", "DB_URL"]   
   for var in LIST_OF_VARIABLE:
      if not os.getenv(var):
           sys.exit()
           print(f"THE {var} ENVIRONMENT VARIABLE IS MISSING.")
else:
   API_ID = 1234567
   API_HASH = "<hash>"
   BOT_TOKEN = "<bot-token>"
   SESSION = "<string-session>"
   GROUP_ID = -1001717881477
   KATSUKI = "https://graph.org/file/56bb59a1057c3021ae8cd.mp4"
   HANDLER = ["~", ".","!","?","@","$"]
   DB_URL = "<mongodb-url>"




SOURCE = "https://github.com/nandhaxd/katsuki"
NAME = "Nandha"


