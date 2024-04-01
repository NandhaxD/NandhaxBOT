"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import os, sys 


""" CHANGE TO FALSE IF YOU DON'T WANNA ADD VARIABLES IN HOSTING SITE """

ENV = os.getenv("ENV", True)



if ENV:    
   API_ID = os.getenv("API_ID", 13257951)
   API_HASH = os.getenv("API_HASH", "d8ea642aedb736d40035bc05f0cfd477")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6059605779:AAGn74wEaCqIvhZxFZQHOjDtKOz51ITi2io")
   SESSION = os.getenv("SESSION")
   GROUP_ID = os.getenv("GROUP_ID", -1001717881477)
   OWNER_ID = os.getenv('OWNER_ID', 5696053228)
   GROUP_LINK = os.getenv('GROUP_LINK', "t.me/nandhasupport")
   DB_URL = os.getenv("DB_URL", "mongodb+srv://nandhaxd:hIatwh7wpArjRPX3@cluster0.80igexg.mongodb.net")
   LANG_CODE = os.getenv('LANG_CODE', 'en')
   LIST_OF_VARIABLE = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION", "GROUP_ID", "DB_URL", "OWNER_ID"]      
else:
   API_ID = 13257951 #int() method | get from my.telegram.org
   API_HASH = "d8ea642aedb736d40035bc05f0cfd477" #str() method | get from my.telegram.org
   BOT_TOKEN = "6059605779:AAGn74wEaCqIvhZxFZQHOjDtKOz51ITi2io" #str() method | get via @botfather
   SESSION = "BQDKTN8AnC-7eeIoBSMj00LSBq5Kn_1yvYg4NdiDxQUheI39wdlGwZ2Z29HU7S8afa7vI_E86SMEebwrMR5CxDFEAvA-vsY5S_cKZm5BkY8l3ECyg5eU4FMRAys6FCCp4RxFo5ycunCReiv-vMUSqwr22V4v73JWHlPJghxROx4s9JDUL3SB0gOFm6HZmBa8MHx86pToJb0HORu69TKjWcArokBmHhqvOq--yIWTJsoDDLIy_Qszk3Km2I21TpU5p9NcGoiALwPryANBu7YPjfMaDPUneagkshX2DTfSa9eSMFAnLv0jwkmPW6FYX0dsXv7qARbN10fxd3Ltjufcg_kJTfvxewAAAAFTgt_sAA" #str() method | use replit or bots to get your Pyro session    GROUP_ID = -1001717881477 #int() menthod | your group id
   DB_URL = "mongodb+srv://nandhaxd:hIatwh7wpArjRPX3@cluster0.80igexg.mongodb.net/" # get from mongodb.com
   GROUP_LINK = "t.me/nandhasupport"
   OWNER_ID = 5696053228 # fill ur user id
   LANG_CODE = 'en'


# DEFAULT VARIABLES 


HANDLER = ["~", ".","!","?","@","$"] 
NAME = "Katsuki"
  

# REQUIRED VARIABLES

SOURCE = "https://github.com/nandhaxd/katsuki"


