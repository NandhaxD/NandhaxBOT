import asyncio
from pyrogram import filters
from pyrogram.types import User, Message
from pyrogram.errors import PeerIdInvalid
from datetime import datetime
from pyrogram.raw import functions

from Katsuki import katsuki
from config import HANDLER, OWNER_ID




INFO = (
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**[{full_name}](tg://user?id={user_id})**"

    "**Usᴇʀ Iᴅ**: `{user_id}`"
    
    "**Fɪʀsᴛ Nᴀᴍᴇ**: `{first_name}`"

    "**Lᴀsᴛ Nᴀᴍᴇ**: `{last_name}`"

    "**Usᴇʀɴᴀᴍᴇ**: `{username}`"

    "**Lᴀsᴛ Oɴʟɪɴᴇ**: `{last_online}`"

    "**Cᴏᴍᴍᴏɴ Gʀᴏᴜᴘs**: `{common_groups}`"
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**Pʀᴏғɪʟᴇ Pɪᴄs**: `ᴜsᴇʀ  ᴅᴏɴ'ᴛ  ʜᴀᴠᴇ  ᴀɴʏ  ᴘʀᴏғɪʟᴇ  ᴘɪᴄ`"

    "**Lᴀsᴛ Uᴘᴅᴀᴛᴇᴅ**: `ᴜsᴇʀ  ᴅᴏɴ'ᴛ  ʜᴀᴠᴇ  ᴀɴʏ  ᴘʀᴏғɪʟᴇ  ᴘɪᴄ`"
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**Bɪᴏ**: {bio}"
)

INFO_PIC = (
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**[{full_name}](tg://user?id={user_id})**"
    
    "**Usᴇʀ Iᴅ**: `{user_id}`"

    "**Fɪʀsᴛ Nᴀᴍᴇ**: `{first_name}`"

    "**Lᴀsᴛ Nᴀᴍᴇ**: `{last_name}`"

    "**Usᴇʀɴᴀᴍᴇ**: `{username}`"

    "**Lᴀsᴛ Oɴʟɪɴᴇ**: `{last_online}`"

    "**Cᴏᴍᴍᴏɴ Gʀᴏᴜᴘs**: `{common_groups}`"
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**Pʀᴏғɪʟᴇ Pɪᴄs**: `{profile_pics}`"

    "**Lᴀsᴛ Uᴘᴅᴀᴛᴇᴅ**: `{profile_pic_update}`"
    "━━━━━━━━━━━━━━━━━━━━━━━━"
    "**Bɪᴏ**: {bio}"
)

def remply(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


def lastonline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.last_online_date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


async def commons(bot: katsuki, get_user):
    common = await bot.send(
        functions.messages.commonsChats(
            user_id=await bot.resolve_peer(get_user), max_id=0, limit=0
        )
    )
    return common


def fullname(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic[0].date).strftime("%d.%m.%Y, %H:%M:%S")


@katsuki.on_message(filters.command("info", prefixes=HANDLER) & filters.user(OWNER_ID))
async def info(bot: katsuki, message: Message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await bot.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("`ɴᴏ  ɪᴅᴇᴀ  ᴡʜᴏ  ᴛʜɪs  ᴜsᴇʀ  ɪs.  ʏᴏᴜ'ʟʟ  ʙᴇ  ᴀʙʟᴇ  ᴛᴏ  ɪɴᴛᴇʀᴀᴄᴛ  ᴡɪᴛʜ  ᴛʜᴇᴍ  ɪғ  ʏᴏᴜ  ʀᴇᴘʟʏ  ᴛᴏ  ᴛʜᴀᴛ  ᴘᴇʀsᴏɴ's  ᴍᴇssᴀɢᴇ  ɪɴsᴛᴇᴀᴅ,  ᴏʀ  ғᴏʀᴡᴀʀᴅ  ᴏɴᴇ  ᴏғ  ᴛʜᴀᴛ  ᴜsᴇʀ's  ᴍᴇssᴀɢᴇs.`")
        await asyncio.sleep(2)
        await message.delete()
        return

    user_details = await bot.get_chat(get_user)
    bio = user_details.bio
    user_pic = await bot.get_profile_photos(user.id)
    pic_count = await bot.get_profile_photos_count(user.id)
    common = await commons(bot, user.id)

    if not user.photo:
        await message.edit(
            INFO.format(
                full_name=fullname(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=lastonline(user),
                common_groups=len(common.chats),
                bio=bio if bio else "`ᴜsᴇʀ  ʜᴀs  ɴᴏ  ʙɪᴏ.`",
            ),
            disable_web_page_preview=True,
        )
    elif user.photo:
        await bot.send_photo(
            message.chat.id,
            user_pic[0].file_id,
            caption=INFO_PIC.format(
                full_name=fullname(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=lastonline(user),
                profile_pics=pic_count,
                common_groups=len(common.chats),
                bio=bio if bio else "`ᴜsᴇʀ  ʜᴀs  ɴᴏ  ʙɪᴏ.`",
                profile_pic_update=ProfilePicUpdate(user_pic),
            ),
            reply_to_message_id=remply(message),
        )

        await message.delete()