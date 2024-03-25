"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import os, sys 


""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", False)



if ENV:    
   API_ID = os.getenv("API_ID")
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   SESSION = os.getenv("SESSION")
   GROUP_ID = os.getenv("GROUP_ID", -1001717881477)
   OWNER_ID = os.getenv('OWNER_ID')
   DB_URL = os.getenv("DB_URL")
   LIST_OF_VARIABLE = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION", "GROUP_ID", "DB_URL", "OWNER_ID"]   
   for var in LIST_OF_VARIABLE:
      if not os.getenv(var):
           sys.exit()
           print(f"THE {var} ENVIRONMENT VARIABLE IS MISSING.")
else:
   API_ID = 13257951 #int() method | get from my.telegram.org
   API_HASH = "d8ea642aedb736d40035bc05f0cfd477" #str() method | get from my.telegram.org
   BOT_TOKEN = "6059605779:AAGn74wEaCqIvhZxFZQHOjDtKOz51ITi2io" #str() method | get via @botfather
   SESSION = "BQDKTN8AuM4Olt5aDWZxxtPugoTAevANp0JMiEDTvKD01pOtzXsI6k1px_F400ApY4RV-m4BEn953pWrCeHz1UT7P4kNniKbueFjL3OQLlueUt1K2ZlTBINH-cYZXDGJcJn5FFUFocDc0G0oikdN3jCm9clHNbIVDoCvUCNY4TjQsG3H2SfHGPAf-zRYY-UFHiRcMCntAHjiVhd5KOpk7W590ogGl5MgnXGahC01QEUW1K16L1B8l_OEFKOaTlGis5QKVQfgHkQNvoPQB4dydV4B-DAtK5YFMgUEUViQitA3rZcUhz2qwO8H3K_byjkfzmoEQ0XccWQK6BEu8gv0EC3dW051GwAAAAFTgt_sAA" #str() method | use replit or bots to get your Pyro session    GROUP_ID = -1001717881477 #int() menthod | your group id
   DB_URL = "mongodb+srv://nandhaxd:u7uHs7EhyuyLT5Kj@cluster0.80igexg.mongodb.net/" # get from mongodb.com
   OWNER_ID = 5696053228 # fill ur user id


# DEFAULT VARIABLES 


HANDLER = ["~", ".","!","?","@","$"] 
NAME = "Katsuki"
  

# REQUIRED VARIABLES

SOURCE = "https://github.com/nandhaxd/katsuki"


