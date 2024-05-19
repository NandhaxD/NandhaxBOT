

from urllib import parse
from nandha import bot
from pyrogram import filters

from nandha.helpers.trhozory import AsyncHozoryTranslator


@bot.on_message(filters.command('tr'))
async def translate (_, message):
     usage = "**Example**: `/tr ja`\nreply to the message and here the [translation code's](https://telegra.ph/Lang-Codes-03-19-3)"
     reply = message.reply_to_message
     if len(message.text.split()) < 2:
         return await message.reply(usage)
     if reply and (reply.text or reply.caption):
          text = reply.text or reply.caption
          code = message.text.split()[1]
          try:
             hozory_engine =  AsyncHozoryTranslator()
             resp = await hozory_engine.translate(text, code)
             tr_text = resp.translated_text
             # audio = resp.voice_link ( useless )
             await message.reply_text(
                       text=(f'🧾** Code**: `{code}`'
                       f'\n\n💫** Translate**:\n\n{tr_text}'))
          except Exception as e:
               return await message.reply(str(e))
     else:
        return await message.reply(usage)
