
# இதை எடுக்கிறவன்‌‌ ஒரு புண்டை

from nandha import bot
from nandha.database.welcome import set_welcome, check_welcome
from nandha.helpers.help_func import make_captcha
from nandha.helpers.decorator import admin_only
from pyrogram import filters, types, enums


import asyncio

temp = {}

welcome_gif = 'https://telegra.ph/file/e8079bbfc854e7458d8c1.mp4'

async def kick_chat_member(chat_id: int, user_id: int):
     try:
        await bot.ban_chat_member(chat_id, user_id)
        await bot.unban_chat_member(chat_id, user_id)
     except:
          pass

def cvt_btn(lst, user_id):
    button_groups = [lst[i:i+3] for i in range(0, len(lst), 3)]
    btns = []
    for group in button_groups:
        row = []
        for text in group:
             row.append(types.InlineKeyboardButton(text, callback_data=f'wel:{text}:{user_id}'))
        btns.append(row)  # Move this line inside the outer loop
    return types.InlineKeyboardMarkup(btns)
    

def remove_entry(temp, chat_id, user_id):
    if user_id in temp and temp[user_id][0] == chat_id:
        del temp[user_id]


def check_token(temp, chat_id, user_id, token):
    for value in temp.values():
        if value[0] == chat_id and value[1] == token:
            return True
    return False





@bot.on_callback_query(filters.regex('^wel'))
async def wel_approve(_, query):
     token = query.data.split(':')[1]
     user_id = int(query.data.split(':')[2])
     chat_id = query.message.chat.id
     if query.from_user.id != user_id:
          return await query.answer("You cannot verify for others.")
     
     approved = check_token(temp, chat_id, user_id, token)
    
     if approved:
          name = query.from_user.mention
          chatname = query.message.chat.title
          try:
              await bot.restrict_chat_member(
                   chat_id=chat_id, 
                   user_id=user_id, 
                   permissions=types.ChatPermissions(
               can_send_messages=True,
               can_send_media_messages=True,
               can_send_polls=True,
               ))
          except Exception as e:
               pass
          text = f'**Hey {name}, Welcome to {chatname} ❤️**'
          await query.message.edit_media(media=(types.InputMediaAnimation(media=welcome_gif, caption=text)))
          remove_entry(temp, chat_id, user_id)
     else:
          return await query.answer('What the fuck Itz wrong are you that much noob?', show_alert=True)
          
     


@bot.on_chat_member_updated(group=4)
async def welcome(_, update):
     
     chat_id = update.chat.id
     user_id = update.from_user.id
     
     is_welcome = await check_welcome(chat_id)
     
     if (
          #not update.old_chat_member and 
          update.new_chat_member.user 
          and not update.new_chat_member.user.is_bot
          and is_welcome 
     ):
              
           mention = update.new_chat_member.user.mention()   
           chatname = update.chat.title
           photo, token, alt = await make_captcha(user_id, chat_id)
           button = cvt_btn(alt, user_id)
           
           text = f'**Hello, {mention} solve the captcha to chat in {chatname}**'
           try:
             await bot.restrict_chat_member(
                  chat_id=chat_id,
                  user_id=user_id, 
                  permissions=types.ChatPermissions(
                       can_send_messages=False
                  ))
           except Exception as e:
                 pass
           remove_entry(temp, chat_id, user_id)
           temp[user_id] = (chat_id, token)
           msg = await bot.send_photo(
                photo=photo,
                chat_id=chat_id, 
                caption=text,
                reply_markup=button
           )
           await asyncio.sleep(2*60)
           token_exsit = check_token(temp, chat_id, user_id, token)
           if token_exsit:
               remove_entry(temp, chat_id, user_id)
               await kick_chat_member(chat_id, user_id)
               await msg.edit(f'**{mention} was kicked for unable to solve captcha.**')
               await asyncio.sleep(60)
               await msg.delete()
               
          



@bot.on_message(filters.command('captcha'))
@admin_only(bot) #bot client
async def captcha(_, message):
    
    if message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply(
               'Only captcha can be used in groups.')

    chat_id = message.chat.id
    
    if len(message.text.split()) < 2:
          kk = await check_welcome(chat_id)
         
          text = 'Example:\n- /captcha on|off'
          text += f'\n\n**Chat welcome captcha: {kk}**'
               
          return await message.reply(text
               )
    else:
        modes = ('on', 'off')
        mode = message.text.split()[1].lower()
        if mode in modes:
             name = message.chat.title
             
             if mode == 'on':
                 await set_welcome(chat_id, True)
                 return await message.reply(
                        f'**Successfully captcha turn on in {name}.** ✅')
             elif mode == 'off':
                  await set_welcome(chat_id, False)
                  return await message.reply(
                        f'**Successfully captcha turn off in {name}.** ✅')
        else:
           return await message.reply(
                'Example:\n- /captcha on|off')
             
             
     

     
