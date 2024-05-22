
from pyrogram import filters, types, enums
from nandha import bot

import requests
import json


headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; Infinix X6816C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
}


data = {
    "userId": "public-access",
    "platform": "landing_demo",
    "ssml": "okay",
    "voice": "en-US-AshleyNeural",
    "narrationStyle": "Neural",
    "method": "file"
}


@bot.on_message(filters.command('voice'))
async def voice(_, message):

    Usage = (
      "Reply to the message text"
    )
    
    reply = message.reply_to_message
    if reply and reply.text:
        data["ssml"] = reply.text
        try:
           response = requests.post(url, headers=headers, json=data, timeout=60)
           resp = response.json()
           voice = resp["file"]
           await bot.send_voice(
              chat_id=message.chat.id,
              voice=voice,
              reply_to_message_id=message.id
                 )
                     
        except Exception as e:
             return await message.reply(str(e))
    return await message.reply(
       Usage
   )



