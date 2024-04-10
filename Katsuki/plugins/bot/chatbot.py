
import config
import requests

from urllib.parse import quote

from Katsuki import bot
from pyrogram import filters, enums


is_chatbot = False

api = 'https://tofu-node-apis.onrender.com/api/charai?charID=gkLVbtXVSkljrRjnkzOowUbfXntEOFB2iWtu3xBj19A&q={}'

@bot.on_message(filters.reply & filters.text & filters.chat(-1001717881477) & ~filters.bot)
async def reply_chatbot(_, message):
      
      chat_id = message.chat.id
      
      if is_chatbot is False:
          return
            
      else:    
          reply = message.reply_to_message
          if reply.from_user and reply.from_user.id == config.BOT_ID:
               name = message.from_user.first_name
               message_text = quote(f'username: {name}\nprompt:\n'+message.text)
               try:
                  response = requests.get(api.format(message_text), timeout=10).json()
               except requests.exceptions.Timeout as e:
                        return 
               try:
                    success = response['reply']
                    if success:
                        await bot.send_chat_action(chat_id, enums.ChatAction.TYPING)
                        await message.reply(success)
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
               'Successfully turn onend chatbot in the chat group.')
         elif query == 'off':
               is_chatbot = False
               return await message.reply(
                  'Successfully turn offend chatbot in the chat group.')
         else:
              return await message.reply(
          'Example: !chatbot on|off')
              




           
