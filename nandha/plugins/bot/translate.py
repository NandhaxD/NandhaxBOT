

from urllib import parse
from nandha import bot
from pyrogram import filters

import requests


@bot.on_message(filters.command('tr'))
async def translate (_, message):
     usage = '**Example**: `/tr ja`\n (reply to the message)'
     reply = message.reply_to_message
     if len(message.text.split()) < 2:
         return await message.reply(usage)
     if reply and reply.text or reply.caption:
          text = reply.text or reply.caption
          code = message.text.split()[1]
          try:
             api = requests.get(f'https://nandha-api.onrender.com/htranslate?text={parse.quote(text)}&code={code}').json()
             tr_text = api['translated_text']
             audio = api['voice_link']
             try:
                 await message.reply_audio(
                       audio=audio, caption=(f'🧾 Code:\n`{code}`'
                       f'\n🧾 Translate:\n{tr_text}'))
             except:
                 await message.reply_text(
                       text=(f'🧾 Code:\n`{code}`'
                       f'\n🧾 Translate:\n{tr_text}'))
          except Exception as e:
               return await message.reply('Error:\n', str(e))
     else:
        return await message.reply(usage)
