import config
import random
import asyncio 
import requests 
from pyrogram import filters, enums
from nandha import bot ,app, lang, DATABASE
from nandha.helpers.help_func import emoji_convert, anime_gif_key, get_anime_gif
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.raw.functions.messages import SetTyping
from pyrogram.raw.types import SendMessageEmojiInteraction, DataJSON


async def click_interaction(bot, message):
    await bot.invoke(
        SetTyping(
            peer=await bot.resolve_peer(message.chat.id),
            action=SendMessageEmojiInteraction(
                emoticon=message.text,
                msg_id=message.id,
                interaction=DataJSON(data='{"v":1, "a": [{"t": 1, "i": 2}]}'),
            ),
        )
    )
     
SPAM = []
emoji = ['⚡️', '❤️', '🥳', '👾', '🔥', '🤑']


@bot.on_message(filters.command("start"))
async def start(_, message):
     user_id = message.from_user.id

     if len(message.text.split()) == 2 and message.text.split(None,1)[1].startswith('getfile') and message.chat.type == enums.ChatType.PRIVATE:
            try:
              token = message.text.split(None, 1)[1].split('-')[-1]
            except Exception as e:
                 return await message.reply(
                      'Your method is invalid try t.me/{botusername}?start=getfile-{token} 🤔.')
                 
            db = DATABASE['LINK_TO_FILE']
            for tokens in db.find():
                 if token in tokens:
                    user_id = tokens['user_id']
                    file_ids = tokens[token]
                 else:
                     return await message.reply(
                          'Invaid token check again 🤔.')
                    
            if file_ids:
                 
                 for i, file_id in enumerate(file_ids):
                      file_num = f"File No: {i+1}"
                      try:
                         await bot.send_document(
                             chat_id=message.from_user.id,
                             document=file_id,
                             caption=file_num,
                             reply_to_message_id=message.id
                        )
                      except ValueError:
                          await bot.send_video(
                             chat_id=message.from_user.id, 
                             video=file_id, 
                             caption=file_num,
                             reply_to_message_id=message.id
                          )
                      await asyncio.sleep(2)
                   
            BUTTON=InlineKeyboardMarkup([[InlineKeyboardButton("GROUP ⬅️", url=config.GROUP_LINK)]])

            upload_by = await bot.get_users(user_id)
            return await message.reply(
                         f'**Successfully uploaded {len(file_ids)} file, Thank you for using me ❤️. Uploaded by [{upload_by.first_name}](tg://user?id={upload_by.id})**',
                    reply_markup=BUTTON)
          

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
           msg = await message.reply(random.choice(emoji))
           await click_interaction(bot, msg)
           await asyncio.sleep(4)
           
           await message.forward(config.OWNER_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣", url=config.GROUP_LINK)]])
     await message.reply_animation(
          animation=animation,
          caption=lang['bot_start_01'].format(mention, applive,botlive), quote=True, reply_markup=BUTTON)
     await asyncio.sleep(5)
     SPAM.remove(user_id)
