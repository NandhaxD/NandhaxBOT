from config import OWNER_ID, HANDLER
from Katsuki import katsuki
from Katsuki.utils import section
from pyrogram import filters 

@katsuki.on_message(filters.command("cinfo",prefixes=HANDLER) & filters.user(OWNER_ID))
async def cinfo(_, m):
       reply = m.reply_to_message
       if not reply:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if not reply.sender_chat:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if reply.sender_chat:
             message = await m.reply_text("information gathering!!!")
             id = reply.sender_chat.id
             type = reply.sender_chat.type
             name = reply.sender_chat.title
             username = reply.sender_chat.username
             pfp = reply.sender_chat.photo
       if not pfp:
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await m.reply_text(text)
            await message.delete()
            return 
       image = reply.sender_chat.photo
       if image:
            photo = await katsuki.download_media(image.big_file_id)
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await katsuki.send_photo(m.chat.id,photo,caption=(text))
            await message.delete()
              
              
              
async def get_user_info(user, already=False):
    if not already:
        userss = await bot.get_chat(user)
        user = await bot.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    is_bot = user.is_bot
    photo_id = user.photo.big_file_id if user.photo else None
    is_dev = user_id in dev_user
    body = { 
        "✪ ID": user_id,
        "✪ DC": dc_id,
        "✪ Name": [first_name],
        "✪ Username": [("@" + username) if username else "Null"],
        "✪ Mention": [mention],
        "✪ Bot": is_bot,
        "✪ Developer": is_dev,
        "✪ Bio": userss.bio,
    }
    caption = section("User info results", body)
    return [caption, photo_id]             


@katsuki.on_message(filters.command("info",prefixes=HANDLSR) & filters.user(OWNER_ID))
async def info_func(_, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Information Processing...")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await katsuki.download_media(photo_id)

    await message.reply_photo(photo=photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)
