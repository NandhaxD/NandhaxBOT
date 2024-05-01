import config
import random
import asyncio 
import requests 
from pyrogram import filters, enums
from nandha import bot ,app, lang, DATABASE
from nandha.helpers.help_func import emoji_convert, anime_gif_key, get_anime_gif
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


SPAM = []

@bot.on_message(filters.command("start"))
async def start(_, message):
     user_id = message.from_user.id

     if len(message.text.split()) == 2 and message.text.split()[1].startswith('file') and message.chat.type == enums.ChatType.PRIVATE:
            token = message.text.split(':')[1]
            db = DATABASE['LINK_TO_FILE']
            user = db.find_one({'user_id': user_id})            
            if user:
               ignore = ['_id', 'user_id']
               user_tokens = [ token for token in db.find_one(user_json) if token not in ignore]
               if token in user_token:
                    file_ids = user[token]
                    
                    for file_id in file_ids:
                        await bot.send_document(
                             chat_id=user_id, document=file_id, quote=True
                        )
                    return await message.reply(
                         f'**Successfully uploaded {len(file_ids)} thank you for using Me.**')
          

     key = random.choice(anime_gif_key)
     animation = await get_anime_gif(key=key)
     
     if user_id in SPAM:
         return await message.reply(lang['bot_start_02'])
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(app.is_connected)
     name = config.NAME
     id = config.OWNER_ID
     SPAM.append(user_id)
     if message.chat.type == enums.ChatType.PRIVATE:
           await message.forward(config.OWNER_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source ⬅️", url=config.SOURCE),InlineKeyboardButton("GROUP ⬅️", url=config.GROUP_LINK)]])
     await message.reply_animation(
          animation=animation,
          caption=lang['bot_start_01'].format(mention, applive,botlive), quote=True, reply_markup=BUTTON)
     await asyncio.sleep(5)
     SPAM.remove(user_id)
