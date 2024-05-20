from nandha import bot
from pyrogram import filters, types, enums
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


import config

switch_btn = types.InlineKeyboardMarkup(
    [[types.InlineKeyboardButton("〔 Secret 〕", switch_inline_query_current_chat="secret ")]]
)

temp = {}

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
    except ValueError:
        await bot.answer_inline_query(
            inline_query_id=inline_query.id,
            results=[
                InlineQueryResultArticle(
                    title="❌ Secret invalid 🥸",
                    input_message_content=InputTextMessageContent(usage)
                )
            ]
        )
        return

    try:
        info = await bot.get_users(to_user)
    except Exception:
          await bot.answer_inline_query(
            inline_query_id=inline_query.id,
            results=[
                InlineQueryResultArticle(
                    title="❌ Secret Username or ID 🥸",
                    input_message_content=InputTextMessageContent(usage)
                )
            ]
        )
          return

    to_name = info.first_name
    to_mention = info.mention
    to_user_id = info.id

    text = (
        f'**👀 {mention} sent a secret message to {to_mention}. Only they can view the message. 🚫**'
    )

    ok = await bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[
            InlineQueryResultArticle(
                title=f"✅ Secret message to {to_name}",
                input_message_content=InputTextMessageContent(text),
                reply_markup=types.InlineKeyboardMarkup([[
                    types.InlineKeyboardButton(
                        'Secret 👀', callback_data=f'secret:{user_id}:{to_user_id}'
                    )
                ]])
            )
        ]
    )

    if ok:
        await add_secret(user_id, to_user_id, message)

@bot.on_callback_query(filters.regex('^secret'))
async def cb_secret(_, query):
    from_user = int(query.data.split(':')[1])
    to_user = int(query.data.split(':')[2])

    if query.from_user.id not in [from_user, to_user]:
        await query.answer("You can't see others' secrets!")
        return

    secret = await get_secret(from_user, to_user)
    if not secret:
        await query.answer("Your secret message has vanished 😭")
        return

    info = await bot.get_users(from_user)
    text = (
        f'{secret[1]}\n\nSecret message by {info.full_name}'
    )
    await query.answer(text, show_alert=True)
