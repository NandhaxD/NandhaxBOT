
from nandha import bot
from pyrogram import filters, types
from datetime import datetime

import config
import requests
import random
import json
import re



BinString = (
  '📛 BIN: #{}\n'
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
           data = req.json()
           if not data.get('country'):
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
         code = message.text.split()[1][:6]
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
         #elif not len(code) == 6:
              # return await message.reply(
               #  'Only 6 digit are Known for Bin.'
             #  )
         else:
            msg = await message.reply('Please wait a movement...')
           
            bin = await bin_info(code)
            if not bin:
                return await msg.edit(
                  'Double check your bin maybe itz invalid.'
                )
            else:
               cc = await generate_random_cc(code, limit)
               credit_cards = '\n'.join(card for card in cc)
               String = f'```\n{credit_cards}```\n💳 Credit Cards: {limit}\n\n' + bin
               return await msg.edit(String)
            
  

@bot.on_message(filters.command('bcheck'))
async def bin_checker(_, message):
     if len(message.text.split()) < 2:
         return await message.reply(
           '**Example**:\n'
           '/bcheck 123456'
         )
     else:
         code = message.text.split()[1][:6]
         if not code.isdigit():
              return await message.reply(
                'Please only digit are allowed.'
              )
         #elif not len(code) == 6:
            #   return await message.reply(
                # 'Only 6 digit are Known for Bin.'
            #   )
         else:
             msg = await message.reply('Please wait a movement...')
             bin = await bin_info(code)
             if not bin:
                 return await msg.edit(
                   'Maybe the bin is invalid try other.'
                 )
             else:
                 await msg.edit(bin)


           



langs = {
    'United State': 'en_US', 'Hong Kong': 'en_HK', 'Nigeria': 'en_NG', 'New Zealand': 'en_NZ', 'South Africa': 'en_ZA', 
    'Saudi Arbia': 'ar_SA', 'Austria': 'at_AT', 'Czech': 'cs_CZ', 'Denmark': 'da_DK', 'Germany': 'de_DE', 'Spain': 'es_ES', 
    'Peru': 'es_PE', 'Iran': 'fa_IR', 'Finland': 'fi_FI', 'Belgium': 'nl_BE', 'Venezuela': 'es_VE', 'France': 'fr_FR', 
    'Israel': 'he_IL', 'Croatia': 'hr_HR', 'Hungary': 'hu_HU', 'Indonesia': 'id_ID', 'Italy': 'it_IT', 'Japan': 'ja_JP', 
    'South Korea': 'ko_KR', 'Lithuania': 'lt_LT', 'Latvia': 'lv_LV', 'Malaysia': 'ms_MY', 'Nepal': 'ne_NP', 
    'Netherlands': 'nl_NL'
}


def fake_generator(county_name: str):
   match = next((country for country in lang.keys() if re.search(re.escape(county_name), county, re.IGNORECASE)), None)
   if match:
       url = 'https://www.softo.org/api/fakeAddressGenerator'
       headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest'}
       payload = {
        'lang': langs[county_name],
        'length': 1,
        'gens': ['streetAddress', 'name', 'phone', 'company', 'credit']}
       json_payload = json.dumps(payload)
       response = requests.post(url, headers=headers, data=json_payload)
       if response.status_code == 200:
            data = response.json()
            return data


@bot.on_message(filters.command(['fk','fake']))
async def fake_info(_, message):
    
     
     example = "**Example**:\n`/fake United State`\n"    
     if len(message.text.split()) == 2:
          data = fake_generator(message.text.split()[1])
          formatted_data = ""
             for key, value in data[0].items():
                  # Add the key-value pair to the formatted string
                  formatted_data += f"**{key.capitalize()}**: `{value}`\n"
          await message.reply_text(
              text=formatted_data, reply_markup=types.InlineKeyboardMarkup(
                types.InlineKeyboardButton(
                  text='By NandhaBots', url='NandhaBots.t.me'
                )
              ))
     else:
        return await message.reply_text(
          text=example+'**Countries**:'+'\n'.join(f"**{name.capitalize()}**" for name in langs.keys())
)

             
 

    

                
