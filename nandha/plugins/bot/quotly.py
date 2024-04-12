import config
import requests
import base64

from pyrogram import filters, enums
from nandha import bot ,app, lang
from nandha.helpers.help_func import grap
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
           if reply.forward_from:
                if not len(message.text.split()) < 2:
                      bg_code = message.text.split()[1]
                else:
                     bg_code = "332255"
                text = reply.text if reply.text else None
                photo_id = reply.forward_from.photo.big_file_id if reply.forward_from.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                username = reply.forward_from.first_name
                avatar_url = await grap(await bot.download_media(photo_id))
                
           elif reply.from_user:
                 if not len(message.text.split()) < 2:
                       bg_code = message.text.split()[1]
                 else:
                       bg_code = "332255"
                 text = reply.text if reply.text else None
                 if text is None:
                     return await message.reply(lang['reply_to_text'])
                 photo_id = reply.from_user.photo.big_file_id if reply.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                 username = reply.from_user.first_name
                 avatar_url = await grap(await bot.download_media(photo_id))
          
           elif not reply:
               if not len(message.text.split()) < 2:
                   try:
                        bg_code = message.text.split(message.text.split()[0])[1].split('|')[0]
                        is_bg_code = True
                   except:
                        bg_code = "332255"
                    
                   text = message.text.split(message.text.split()[0])[1].split('|')[1] if is_bg_code == True else message.text.split(None, 1)[1]
                   username = message.from_user.first_name
                   photo_id = message.from_user.photo.big_file_id if message.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                   avatar_url = await grap(await bot.download_media(photo_id))
           else:
               return await message.reply(lang['context'])

           data['backgroundColor'] = bg_code
           data['messages'][0]['from']['name'] = username
           data['messages'][0]['from']['photo']['url'] = avatar_url
           data['messages'][0]['text'] = text
           response = requests.post('https://bot.lyo.su/quote/generate', json=data).json()
           buffer = base64.b64decode(response['result']['image'].encode('utf-8'))
           name = f"{username}bot.webp"
           open(name, 'wb').write(buffer)
           BUTTON=InlineKeyboardMarkup([[
           InlineKeyboardButton("BG CODE ⬅️", url="https://graph.org/file/1e3df8ff41d67db1fc9ea.jpg")]])
           return await message.reply_sticker(sticker=name, reply_markup=BUTTON, quote=True)

