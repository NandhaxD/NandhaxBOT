from telegraph import upload_file
from pyrogram import filters
from Katsuki import katsuki
from config import HANDLER,  OWNER_ID

@katsuki.on_message(filters.command("tm",prefixes=HANDLER) & filters.user(OWNER_ID))
async def tm(_,message):
    reply = message.reply_to_message
    if not reply:
          return await message.reply_text("Reply to a **Media** to get a permanent telegra.ph link.")
    if not reply.media:
          return await message.reply_text("Reply to a **Media** to get a permanent telegra.ph link.")
    if reply.media:
        msg = await message.reply_text("downloading")
        path = await reply.download()
        await msg.edit("uploading")
        fk = upload_file(path)
        for x in fk:
           url = "https://telegra.ph" + x
    if url.endswith("jpg"):
             await reply.reply_photo(url,caption=f"{url}")
    elif url.endswith("mp4"):
             await reply.reply_animation(url,caption=f"{url}")
    await msg.delete()
