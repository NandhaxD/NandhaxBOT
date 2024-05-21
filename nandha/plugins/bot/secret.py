from nandha import bot
from pyrogram import filters, types, enums, errors
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

import config

temp = {}

switch_btn = types.InlineKeyboardMarkup(
    [[types.InlineKeyboardButton("〔 Secret 〕", switch_inline_query_current_chat=f"secret")]])
 
async def send_inline_query_article(bot, inline_query_id, title, message_content, reply_markup=None):
    try:
         ok = await bot.answer_inline_query(
        inline_query_id=inline_query_id,
        results=[
            InlineQueryResultArticle(
                title=title,
                input_message_content=InputTextMessageContent(message_content),
                reply_markup=reply_markup)])
         return ok
    except errors.EntityBoundsInvalid:
          pass
          return





async def clear_secret(user_id: int, to_user_id: int):
    if user_id not in temp:
        temp[user_id] = []
    data = temp.get(user_id, [])
    if not data:
        return
    for user in data:
        if user[0] == to_user_id:
            data.remove(user)
            break

async def add_secret(user_id: int, to_user_id: int, message: str):
    await clear_secret(user_id, to_user_id)
    temp[user_id].append((to_user_id, message))

async def get_secret(user_id, to_user_id):
    data = temp.get(user_id, [])
    if not data:
        return None
    for user in data:
        if user[0] == to_user_id:
            return user
    return None

@bot.on_message(filters.command('secret'))
async def send_secret(_, message):
    user = message.from_user.username or message.from_user.id
    
    if message.chat.type != enums.ChatType.PRIVATE:
        await message.reply(
            text='Click the button to send secret messages',
            reply_markup=switch_btn
        )
    else:
        await message.reply('Only for chats!')

@bot.on_inline_query(filters.regex('secret'))
async def inline_secret(_, inline_query):
    user_id = inline_query.from_user.id
    name = inline_query.from_user.first_name
    mention = inline_query.from_user.mention

    usage = (
        'Invalid Method! ❌\n'
        f'**Example**:\n`@{config.BOT_USERNAME} secret <username/id> <message>`'
    )

    try:
        _, to_user, message = inline_query.query.split(None, 2)
      
        if len(message) > 180:
             await send_inline_query_article(
                bot=bot, 
                inline_query_id=inline_query.id, 
                title='❌ Invalid message too long', 
                message_content=(
                "🚫 The message you try to send is too large only 170 characters are supposed to sent."), 
                reply_markup=switch_btn
             )  
             return
        
    except ValueError:
        await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title='❌ Invalid method', 
          message_content=usage, 
          reply_markup=switch_btn
        )  
        return

    try:
        info = await bot.get_users(to_user)
    except Exception:
          await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title='❌ PEER ID INVALID', 
          message_content=(
            "⛔ Double check the username or id maybe itz invalid!"),
          reply_markup=switch_btn
          )
          return

    if info.is_bot or info.id == user_id:
         await send_inline_query_article(
            bot=bot, 
            inline_query_id=inline_query.id, 
            title='❌ You cannot do you that.', 
            message_content=(
              "🚫 You can't send a secret message to bots or yourself beware 💀"
            ), 
            reply_markup=switch_btn
         )
         return
    to_name = info.first_name
    to_mention = info.mention
    to_user_id = info.id

    text = (
        f'**👀 {mention} sent a secret message to {to_mention}. Only they can view the message. 🚫**'
    )

    button = reply_markup=types.InlineKeyboardMarkup([[
                    types.InlineKeyboardButton(
                        'Secret 👀', callback_data=f'secret:{user_id}:{to_user_id}'
                    )
                ]])
    
    ok = await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title=f'✅ Secret message to {to_name}\nTap here to sent.', 
          message_content=text, 
          reply_markup=button
    )
    if ok:
        await add_secret(user_id, to_user_id, message)

@bot.on_callback_query(filters.regex('^secret'))
async def cb_secret(_, query):
    from_user = int(query.data.split(':')[1])
    to_user = int(query.data.split(':')[2])

    if query.from_user.id not in [from_user, to_user]:
        await query.answer("You can't see others secrets!")
        return

    secret = await get_secret(from_user, to_user)
    if not secret:
        await query.answer("Your secret message has vanished 😭")
        return

    info = await bot.get_users(from_user)
    text = (
        f'{secret[1]}\n\nSecret message by {info.first_name}'
    )
    await query.answer(text, show_alert=True)
    
