
# இதை எடுக்கிறவன்‌‌ ஒரு புண்டை

from nandha import bot
from nandha.database.welcome import set_welcome, check_welcome
from nandha.helpers.help_func import make_captcha
from pyrogram import filters, types


temp = {}

def covt_btn(list, user_id):
    button_groups = [list[i:i+3] for i in range(0, len(list), 3)]
    btns = []
    for group in button_groups:
        row = []
        for text in group:
             row.append(types.InlineKeyboardButton(text, callback_data=f'wel:{text}:{user_id}'))
    btns.append(row)
    return types.InlineKeyboardMarkup(btns)


def check_token(chat_id: int, user_id: int, token):
   token_d = None
   for key, value in temp.items():
       if value[0] == user_id and key == chat_id:
           token_d = value[1]
           break

   if not token_d:
        return False
   elif taken != token_d:
        return False
   else:
        return True



@bot.on_callback_query(filters.regex('^wel'))
async def wel_approve(_, query):
     token = query.data.split(':')[1]
     user_id = int(query.data.split(':')[2])
     chat_id = query.message.chat.id
     if query.from_user.id != user_id:
          return await query.answer("You cannot verify for others.")
     
     approved = await check_token(chat_id, user_id, token)
    
     if approved:
          name = query.from_user.mention
          chatname = query.message.chat.title
          await query.message.edit(f'Hey {name}, welcome to {chatname}')
     else:
          return await query.answer('What the fuck itz wrong are you that much noob?', show_alert=True)
          
     


@bot.on_chat_member_updated(group=4)
async def welcome(_, update):
     chat_id = update.chat.id
     user_id = update.from_user.id
     
     is_welcome = await check_welcome(chat_id)
     if update.new_chat_member and is_welcome:
          
           mention = update.new_chat_member.user.mention()
           photo, token, alt = await make_captcha(user_id, chat_id)
           button = cvt_btn(alt, user_id)
          
           text = f'Hello, {mention} solve the captcha.'
           await bot.send_photo(
                photo=photo,
                chat_id=chat_id, 
                caption=text,
                reply_markup=button
           )
