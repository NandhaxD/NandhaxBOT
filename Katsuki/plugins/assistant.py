
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



import config
import asyncio, random
import requests
import base64

from pyrogram import filters, enums
from Katsuki import bot ,app, lang
from Katsuki.helpers.help_func import emoji_convert, anime_gif_key, get_anime_gif, grap
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


SPAM = []

@bot.on_message(filters.command("start"))
async def start(_, message):
     user_id = message.from_user.id

     key = random.choice(anime_gif_key)
     animation = await get_anime_gif(key=key)
     
     if user_id in SPAM:
         return await message.reply(lang['bot_start_02'])
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(app.is_connected)
     name = config.NAME
     id = config.OWNER_ID
     SPAM.append(user_id)
     await message.forward(config.OWNER_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source ⬅️", url=config.SOURCE),InlineKeyboardButton("GROUP ⬅️", url=config.GROUP_LINK)]])
     await message.reply_animation(
          animation=animation,
          caption=lang['bot_start_01'].format(mention, applive,botlive), quote=True, reply_markup=BUTTON)
     await asyncio.sleep(10)
     SPAM.remove(user_id)



data = {
  "type": "quote",
  "format": "webp",
  "backgroundColor": None,
  "width": 512,
  "height": 768,
  "scale": 2,
  "messages": [
    {
      "entities": [],
      "avatar": True,
      "from": {
        "id": 1,
        "name": None,
        "photo": {
          "url": None
        }
      },
      "text": None,
      "replyMessage": {}
    }
  ]
}


@bot.on_message(filters.command('q', prefixes=config.HANDLER))
async def quote(_, message):
     reply = message.reply_to_message
     if reply:
           if not len(message.text.split()) < 2:
                 bg_code = message.text.split()[1]
           else:
                 bg_code = "332255"
           text = reply.text if reply.text else None
           if text is None:
                 return await message.edit(lang['reply_to_text'])
           photo_id = reply.from_user.photo.big_file_id if reply.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
           username = reply.from_user.first_name
           avatar_url = await grap(await app.download_media(photo_id))
          
     else:
         if not len(message.text.split()) < 2:
               try:
                  bg_code = message.text.split(message.text.split()[0])[1].split('|')[0]
                  is_bg_code = True
               except:
                    bg_code = "332255"
                    
               text = message.text.split(message.text.split()[0]).split('|')[1] if is_bg_code == True else message.text.split(None, 1)[1]
               username = message.from_user.first_name
               photo_id = message.from_user.photo.big_file_id if message.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
               avatar_url = await grap(await app.download_media(photo_id))

     data['backgroundColor'] = bg_code
     data['messages'][0]['from']['name'] = username
     data['messages'][0]['from']['photo']['url'] = avatar_url
     data['messages'][0]['text'] = text
     response = requests.post('https://bot.lyo.su/quote/generate', json=data).json()
     buffer = base64.b64decode(response['result']['image'].encode('utf-8'))
     name = f"{username}.webp"
     open(name, 'wb').write(buffer)
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("BG CODE ⬅️", url="https://graph.org/file/1e3df8ff41d67db1fc9ea.jpg")]])
     return await message.reply_sticker(sticker=name, reply_markup=BUTTON, quote=True)
     
