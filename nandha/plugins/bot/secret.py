
from nandha import bot
from pyrogram import filters, types, enums
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


switch_btn = types.InlineKeyboardMarkup([[types.InlineKeyboardButton("〔 Secret 〕", switch_inline_query_current_chat="secret ")]])


temp = {}


async def clear_secret(user_id: int, to_user_id: int):
    if not user_id in temp:
        temp[user_id] = []
    data = temp[user_id]
    if not data:
       return
    for user in data:
       if user[0] == to_user_id:
             data.remove(user)
             break
           

async def add_secret(user_id: int, to_user_id: int, message: str):
    await clear_secret(user_id, to_user_id)
    temp[user_id].append((to_user_id, message))


@bot.on_message(filters.command('secret'))
async def send_secret(_, message):
    if message.chat.type != enums.ChatType.PRIVATE:
         await message.reply(
          text='click the button to send secret messages',
          reply_markup=switch_btn)
    else:
       return await message.reply(
           'Only for chats!')


@bot.on_inline_query(filters.regex('secret'))
async def cb_secret(_, inline_query):
      user_id = inline_query.from_user.id
      name = inline_query.from_user.first_name
      mention = inline_query.from_user.mention
  
      usage = (
        'Invliad Method! ❌\n'
        '**Example**:\n@botusername secret nandha fuck'
      )
      try:
          to_user = inline_query.query.split()[1]
          message = inline_query.query.split(None, 2)[1]
      except IndexError:
          await bot.answer_inline_query(
              inline_query_id=inline_query.id,
              results=[
             InlineQueryResultArticle(
                 "❌ Secret invalid 🥸",
             InputTextMessageContent(usage))])

      try:
         info = await bot.get_users(to_user)
      except:
         return
         
      to_name = info.first_name
      to_mention = info.mention
      to_user_id = info.id
  
      text = (
        f'**👀 {mention} send a secret message to {to_mention} only she/he can view the message. 🚫**'
      )
      ok = await bot.answer_inline_query(
              inline_query_id=inline_query.id,
              results=[
             InlineQueryResultArticle(
                 f"✅ Secret messages to  {to_name}",
             InputTextMessageContent(text),
             reply_markup=types.InlineKeyboardMarkup([[
                types.InlineKeyboardButton(
                  'Secret 👀', callback_data=f'secret:{user_id}:{to_user_id}'
                )]]
             ))])
      if ok:
          await add_secret(user_id, to_user_id, message)






      
      
