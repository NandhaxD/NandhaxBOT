from nandha import bot
from pyrogram import filters, types, enums, errors
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, CallbackQuery, InlineQuery

import config

temp = {}


__mod_name__ = "Secret"

__help__ = """

✨ ** Secret Message**:

Example: 
⚡ only work in chats or channel.

`@{BOT_USERNAME} sec {target-id} message`

"""


example= f"""
**Secret Message**:
This type of message is used in public chat to contact people for one-on-one conversations.
No one else can see these messages except the intended recipient, using the bot features.

**Example**:
`@{config.BOT_USERNAME} secret username message`

*Username*: Provide the username of the person to send the secret message to.
*Message*: The secret message text.

**Copy the example above and edit it as needed.**

**You will receive this message again if you do any mistakes of the following**:

Username: Must be a user and not a bot or yourself. Alternatively, you can use the user's ID.
Message: Text must be no longer than 180 characters (e.g., "hello" is 5 characters).

**This module only works for group chats.**
"""




switch_btn = types.InlineKeyboardMarkup(
    [[types.InlineKeyboardButton("〔 Send Secret 〕", switch_inline_query_current_chat=f"secret")]])
 
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
    
    if not message.chat.type in (enums.ChatType.PRIVATE, enums.ChatType.BOT):
        await message.reply(
            text='Click the button to send secret messages',
            reply_markup=switch_btn
        )
    else:
        await message.reply("You can't use in private chats")

@bot.on_inline_query(filters.regex(r'secret|sec'), group=99)
async def inline_secret(_, inline_query: InlineQuery):
    user_id = inline_query.from_user.id
    name = inline_query.from_user.first_name
    mention = inline_query.from_user.mention
    try:
        _, to_user, message = inline_query.query.split(None, 2)
      
        if len(message) > 180:
             await send_inline_query_article(
                bot=bot, 
                inline_query_id=inline_query.id, 
                title='❌ Invalid! message too long', 
                message_content=example, 
                reply_markup=switch_btn
             )  
             return
        
    except ValueError:
        await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title='❌ Invalid! method', 
          message_content=example, 
          reply_markup=switch_btn
        )  
        return

    try:
        info = await bot.get_users(to_user)
    except Exception:
          await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title='❌ No username found', 
          message_content=example,
            reply_markup=switch_btn
          )
          return

    if info.is_bot or info.id == user_id or inline_query.chat_type == enums.ChatType.PRIVATE:
         await send_inline_query_article(
            bot=bot, 
            inline_query_id=inline_query.id, 
            title='❌ You cannot do you that.', 
            message_content=example, 
            reply_markup=switch_btn
         )
         return
    to_name = info.first_name
    to_mention = info.mention
    to_user_id = info.id

    text = (
        f'**👀 {mention} sent a secret message to {to_mention}. Only they can view the message. 🚫**'
    )

    button = types.InlineKeyboardMarkup(
      [[
              types.InlineKeyboardButton(
                        text='Read 👀', callback_data=f'secret:{user_id}:{to_user_id}'),
              types.InlineKeyboardButton(
                          text='Del ⛔', callback_data=f'delsecret:{user_id}:{to_user_id}')
      ]]
)
    
    ok = await send_inline_query_article(
          bot=bot, 
          inline_query_id=inline_query.id, 
          title=f'✅ Secret message to {to_name}\nTap here to sent.', 
          message_content=text, 
          reply_markup=button
    )
    if ok:
        await add_secret(user_id, to_user_id, message)


@bot.on_callback_query(filters.regex('^delsecret'))
async def cb_del_secret(_, query: CallbackQuery):
    from_user = int(query.data.split(':')[1])
    to_user = int(query.data.split(':')[2])
    name = query.from_user.first_name
  
    if query.from_user.id not in [from_user, to_user]:
         await query.answer(
           "You can't delete others secrets!")
         return
    try:
       await query.edit_message_text(f"~~Secret message deleted by {name}~~")
    except:
        await query.answer(
          "I couldn't delete the secret 🤔"
        )
    await clear_secret(from_user, to_user)



@bot.on_callback_query(filters.regex('^secret'))
async def cb_secret(_, query: CallbackQuery):
    from_user = int(query.data.split(':')[1])
    to_user = int(query.data.split(':')[2])

    if query.from_user.id not in [from_user, to_user]:
        await query.answer("You can't see others secrets!")
        return

    secret = await get_secret(from_user, to_user)
    if not secret:
        await query.answer("Your secret message was vanished 😭")
        return

    info = await bot.get_users(from_user)
    text = (
        f'{secret[1]}\n\nSecret message by {info.first_name}'
    )
    await query.answer(text, show_alert=True)
    

