
# இதை எடுக்கிறவன்‌‌ ஒரு புண்டை

from nandha import bot
from pyrogram import filters

@bot.on_chat_member_updated(group=4)
async def welcome(_, update):
     chat_id = update.chat.id
     user_id = update.from_user.id
     if update.new_chat_member :
           #photo, token, alt = await make_captcha(user_id, chat_id)
          
           await bot.send_message(
                chat_id=chat_id, text='Hi,'+update.new_chat_member.user.mention())
