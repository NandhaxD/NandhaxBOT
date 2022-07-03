from Katsuki import katsuki
from config import HANDLER, OWNER_ID




@katsuki.on_message(filters.command("write", prefixes=HANDLER) & filters.user(OWNER_ID))
async def write(_, message):
    if len(message.command) < 2 :
            return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    m = await message.reply_text("ᴡʀɪᴛɪɴɢ...")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ...")
    await m.delete()
    await message.reply_photo(hand, caption = "**ᴍᴀᴅᴇ ʙʏ ᴋᴀᴛsᴜᴋɪ**")
