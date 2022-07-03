from pyrogram import filters
from config import HANDLER, OWNER_ID
from Katsuki import katsuki


@katsuki.on_message(filters.command("webss",perfixes=HANDLER) & filters.user(OWNER_ID))
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "**» ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ...**"
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**» ᴛʀʏɪɴɢ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        await m.edit("**» ᴜᴩʟᴏᴀᴅɪɴɢ ᴄᴀᴩᴛᴜʀᴇᴅ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("**» ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ.**")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
