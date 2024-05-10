
from nandha import bot
from pyrogram import filters

import config
import requests


BinString = (
  '🌍 **Country**: {} {}\n'
  '🏦 **Bank**: {}\n'
  '💳 **Card type**: {}\n'
  '💰 **Card brand**: {}\n'
  '💼 **Scheme**: {}\n'
  '🔒 **Prepaid**: {}\n'
)

async def bin_info(code):
    api = f'https://lookup.binlist.net/{code}'
    req = requests.get(api)
    if req.status_code == 200:
           try:
             data = req.json()
           except:
             return False          
           country = data.get("country", {}).get("name", "")
           emoji = data.get("country", {}).get("emoji", "")
           card_type = data.get("type", "")
           card_brand = data.get("brand", "")
           bank = data.get("bank", {}).get("name", "")
           scheme = data.get("scheme", "")
           prepaid = data.get("prepaid", False)
           return BinString.format(
             emoji, country, bank, card_type, card_brand, scheme, prepaid
           )
    else:
       return False
     
  
  

@bot.on_message(filters.command('bcheck'))
async def bin_checker(_, message):
     if len(message.text.split()) < 2:
         return await message.reply(
           '**Example**:\n'
           '/bcheck 123456'
         )
     else:
         code = message.text.split()[1]
         if not code.isdigit():
              return await message.reply(
                'Please only digit are allowed.'
              )
         elif not len(code) == 6:
               return await message.reply(
                 'Only 6 digit are Known for Bin.'
               )
         else:
             nandha = await bin_info(code)
             if not nandha:
                 return await message.reply(
                   'Sorry Maybe the card is invalid type check again.'
                 )
             else:
                 await message.reply(nandha)


           


                
