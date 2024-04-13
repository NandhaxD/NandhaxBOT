
import config
import requests

from urllib.parse import quote

from nandha import bot
from pyrogram import filters, enums


api = 'https://tofu-node-apis.onrender.com/api/charai?charID=isvAKdyuaL5wGF3BkuJGWu7Rls7q8DAu3bIEIvWOo-Y&q={}'

@bot.on_message(filters.reply & filters.text & filters.chat(config.GROUP_ID) & ~filters.bot)
async def reply_chatbot(_, message):

      # This chatbot module will work only in your group chat. CUSTOMIZED AI
      
          chat_id = message.chat.id    
          reply = message.reply_to_message
          if reply.from_user and reply.from_user.id == config.BOT_ID:
               name = message.from_user.first_name
               message_text = quote(f'{name}:'+message.text)
               try:
                  response = requests.get(api.format(message_text), timeout=10).json()
               except requests.exceptions.Timeout as e:
                        return 
               try:
                    success = response['reply']
                    if success:
                        await bot.send_chat_action(chat_id, enums.ChatAction.TYPING)
                        return await message.reply(success)
               except:
                   return message.reply('What?')
        
