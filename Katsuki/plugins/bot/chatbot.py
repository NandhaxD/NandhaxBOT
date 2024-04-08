
import config
import requests

from urllib.parse import quote

from Katsuki import bot
from pyrogram import filters


is_chatbot = False

api = 'https://tofu-node-apis.onrender.com/api/charai?charID=gkLVbtXVSkljrRjnkzOowUbfXntEOFB2iWtu3xBj19A&q={}'

@bot.on_message(filters.reply & filters.text & filters.chat(-1001717881477) & ~filters.bot)
async def reply_chatbot(_, message):
      if is_chatbot is False:
          return
      else:    
          reply = message.reply_to_message
          if reply.from_user.id == config.BOT_ID:
               message_text = quote(message.text)
               response = requests.get(api.format(message_text)).json()
               try:
                  text = response['reply']
                  await message.reply(text)
               except:
                   return 
        



@bot.on_message(filters.command('chatbot', prefixes=config.HANDLER))
async def chatbot(_, message):
    global is_chatbot
    if len(message.text.split()) < 2:
        return await message.reply(
          'Example: !chatbot on|off')
    else:
         query = message.text.split()[1].lower()
         if query == 'on':
             is_chatbot = True
             return await message.reply(
               'Successfully turn onend the chatbot.')
         elif query == 'off':
               is_chatbot = False
               return await message.reply(
                  'Successfully turn offend the chatbot.')
         else:
              return await message.reply(
          'Example: !chatbot on|off')
              




           
