
# இதை எடுக்கிறவன்‌‌ ஒரு புண்டை

from nandha import bot
from pyrogram import filters

@bot.on_chat_member_updated(group=4)
async def welcome(_, message):
     if message.new_chat_member:
           await message.reply(message.new_chat_member)
