
from nandha import bot
from pyrogram import filters, types, enums
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton("〔 Secret 〕", switch_inline_query_current_chat="wspr ")]])


temp = {}


async def clear_secret(user_id, to_user_id):
    if not user_id in temp:
        temp[user_id] = []
    data = temp[user_id]
    if not data:
       return
    for user in data:
       if to_user_id in user:
             data.remove(user)
             break



async def add_secret(user_id, to_user_id, message):
      await clear_secret(user_id, to_user_id)
      temp[user_id] = (to_user_id, message)
  

@bot.on_message(filters.command('secret'))
async def send_secret(_, message):
    if message.chat.type != enums.ChatType.PRIVATE:
         await message.reply(
          text='click the button to send secret messages',
          reply_markup=types.InlineKeyboardMarkup(switch_btn))
    else:
       return await message.reply(
           'Only for chats!')


@bot.on_inline_query(filters.regex('secret'))
async def cb_secret(_, inline_query):
      user_id = inline_query.from_user.id
      name = inline_query.from_user.first_name
    
      usage = (
        'Invliad Method!\n'
        '**Example**:\n@botusername secret nandha fuck'
      )
      try:
          to_user = inline_query.query.split()[1]
          message = inline_query.query.split(None, 2)[1]
      except IndexError:
          await bot.answer_inline_query(
              inline_query_id,
              results=[
             InlineQueryResultArticle(
                 "Secret 🥸",
             InputTextMessageContent(usage))])

      try:
        info = await bot.get_users(to_user)
      except:
         pass
      to_name = info.first_name
      to_user_id = info.id
  
      await bot.answer_inline_query(
              inline_query_id,
              results=[
             InlineQueryResultArticle(
                 f"✅ Send Secret messages to  {to_name}",
             InputTextMessageContent(usage),
             reply_markup=types.InlineKeyboardMarkup([[
                types.InlineKeyboardButton(
                  'Secret 💀', callback_data=f'secret:{user_id}:{to_user_id}'
                )]]
             ))])
      await add_secret(user_id, to_user_id, message)






      
      
