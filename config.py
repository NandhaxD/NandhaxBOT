

import os, sys


""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", True)


if ENV:    
   API_ID = os.getenv("API_ID")
   API_HASH = os.getenv("API_HASH")
   TOKEN = os.getenv("TOKEN")
   SESSION = os.getenv("SESSION")
   OWNER_ID = os.getenv("OWNER_ID")
   GROUP_ID = os.getenv("GROUP_ID")
   KATSUKI = os.getenv("KATSUKI")
   DB_URL = os.getenv("DB_URL")
   HANDLER = str(os.getenv("HANDLER")).split(",")
   LIST_OF_VARIABLE = ["API_ID", "API_HASH", "TOKEN", "SESSION", "OWNER_ID", "GROUP_ID", "KATSUKI", "HANDLER", "DB_URL"]   
   for var in LIST_OF_VARIABLE:
      try:
          locals()[var] = os.getenv(var)
      except KeyError:
          print(f"The {var} environment variable is missing.")
else:
   API_ID = 1234567
   API_HASH = "<hash>"
   TOKEN = "<bot-token>"
   SESSION = "<string-session>"
   OWNER_ID = 5696053228
   GROUP_ID = -1001717881477
   KATSUKI = "https://graph.org/file/56bb59a1057c3021ae8cd.mp4"
   HANDLER = ["~", ".","!","?","@","$"]
   DB_URL = "<mongodb-url>"




SOURCE = "https://gitHub.com/nandhaxd/katsuki"



