
from pyrogram import filters, types, enums
from nandha import bot

import requests
import json


url = "https://play.ht/api/transcribe"


headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; Infinix X6816C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
}





english_voices = [
   'Guy', 'Amber', 'Eric', 'Lucas',
   'Sara', 'Tony', 'Victoria'
]
  
@bot.on_message(filters.command('voice'))
async def voice(_, message):

    Usage = (
      "Reply to the message text"
    )

    user_id = message.from_user.id
  
    reply = message.reply_to_message
    if reply and reply.text:
        try:
           buttons = [
types.InlineKeyboardButton(str(x), callback_data=str(f'voice:{user_id}:{x}')) for x in (english_voices)
]

           buttons = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
          
           await bot.send_message(
              chat_id=message.chat.id,
              text=(
                reply.text+"\n\n**➲ Click the voice you wanted ❤️**"
              ),
              reply_to_message_id=message.id,
              reply_markup=types.InlineKeyboardMarkup(
                  buttons
              )
                 )
                     
        except Exception as e:
             return await message.reply(str(e))
    else:
        return await message.reply_text(
           text=Usage
   )


@bot.on_callback_query(filters.regex('^voice'))
async def cb_voice(_, query):
     user_id = int(query.data.split(":")[1])
     char_id = query.data.split(":")[2]
     if query.from_user.id != user_id:
         return await query.answer(
                'You cannot access other requests.'
            )
     else:

        text =  query.message.text.split('➲')[0]
        data = {
    "userId": "public-access",
    "platform": "landing_demo",
    "ssml": text,
    "voice": f"en-US-{char_id}Neural",
    "narrationStyle": "Neural",
    "method": "file"
        }
        try:
            await query.message.edit(
              f"**Sending {char_id} voice ❤️.**"
            )
            response = requests.post(url, headers=headers, json=data, timeout=60)
            resp = response.json()
            voice = resp["file"]
            chat_id = query.message.chat.id
            await bot.send_voice(
                chat_id, voice, reply_to_message_id=query.message.id
            )
            await query.message.delete()
        
        except Exception as e:
            return await query.message.edit(str(e))
     
      
     

