
from nandha import bot
from pyrogram import filters
from datetime import datetime

import config
import requests
import random



BinString = (
  '#{}\n'
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
             code, emoji, country, bank, card_type, card_brand, scheme, prepaid
           )
    else:
       return False


async def generate_random_cc(bin_code, limit: int):
    bin_length = len(bin_code)
    if bin_length != 6 or not bin_code.isdigit():
        return "Invalid BIN code format. Please provide a 6-digit number."

    current_year = datetime.now().year
    cc_list = []
    for _ in range(limit):
        cc_number = str(bin_code) + ''.join([str(random.randint(0, 9)) for _ in range(10)])
        cc_expiry_year = random.randint(current_year, current_year + 8)  # Generate expiry year above or equal to the current year
        cc_expiry = str(random.randint(1, 12)).zfill(2) + '|' + str(cc_expiry_year) + '|' + str(random.randint(100, 999))
        cc_info = cc_number + '|' + cc_expiry
        cc_list.append(cc_info)
    
    return cc_list
     





@bot.on_message(filters.command('gencc'))
async def cc_generator(_, message):
     if len(message.text.split()) < 2:
         return await message.reply(
           '**Example**:\n'
           '/gencc 123456 5'
         )
     else:
         code = message.text.split()[1]
         try:
            limit = int(message.text.split()[2])
         except:
             return await message.reply(
           '**Example**:\n'
           '/gencc 123456 5'
             )
         if not code.isdigit():
              return await message.reply(
                'Please only digit are allowed.'
              )
         elif not len(code) == 6:
               return await message.reply(
                 'Only 6 digit are Known for Bin.'
               )
         else:
            bin = await bin_info(code)
            if not bin:
                return await message.reply(
                  'Double check your cc maybe itz invalid.'
                )
            else:
               cc = await generate_random_cc(code, limit)
               credit_cards = '\n'.join(card for card in cc)
               String = f'```Credit Cards: {limit}\n{credit_cards}```\n\n' + bin
               return await message.reply(String)
            
  

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


           


                
