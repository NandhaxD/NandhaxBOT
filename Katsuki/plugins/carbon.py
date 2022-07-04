from pyrogram.types import Message
from pyrogram import filters
from Katsuki import katsuki, aiohttpsession as aiosession
from asyncio import gather
from config import OWNER_ID, HANDLER
from io import BytesIO


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@katsuki.on_message(filters.command("carbon",prefixes=HANDLER) & filters.user(OWNER_ID))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.")
    if not message.reply_to_message.text:
        return await message.reply_text("ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.")
    m = await message.reply_text("😴 ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀʀʙᴏɴ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ...")
    await katsuki.send_photo(message.chat.id, carbon,caption="   ( [ᴍᴀᴅᴇ  ʙʏ  ᴋᴀᴛsᴜᴋɪ ᴛᴇᴀᴍ](https://t.me/team_katsuki) )")
    await m.delete()
    carbon.close()
