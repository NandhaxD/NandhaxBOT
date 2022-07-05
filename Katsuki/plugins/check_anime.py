

import pyrogram
from Katsuki import katsuki
from pyrogram import Client, filters
import asyncio
import tracemoepy
import mimetypes
import requests
import config

DOWNLOAD_DIR = "./downloads"




async def tracemoe_trace(file_path=None, link=None):
    if link:
        async with tracemoepy.AsyncTrace() as tracemoe:
            resp = await tracemoe.search(link, is_url=True)
            content = resp.result[0]
            msg = f"Title: {content.anilist.title.romaji}\n"
            msg += f"Adult: {content.anilist.isAdult}\n"
            msg += f"Episode: {content.episode}\n"
            msg += f"Similarity: {content.similarity*100}\n"
            try:
                video = content.video
            except:
                video = None
    else:
        mt = mimetypes.guess_type(file_path)
        r = requests.post("https://api.trace.moe/search",
            data=open(file_path, "rb"),
            headers={"Content-Type": f"{mt[0]}"}
        ).json()
        msg = f"Title: {r['result'][0]['filename']}\n"
        msg += f"Episode: {r['result'][0]['episode']}\n"
        msg += f"Similarity: {r['result'][0]['similarity']*100}"
        try:
            video = r["result"][0]["video"]
        except:
            video = None
    return msg, video

@katsuki.on_message(filters.command("check_anime",prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def trace_anime_moe(bot: katsuki, update):
    if update.reply_to_message:
        init_msg = await bot.send_message(
            chat_id=update.chat.id,
            text="Downloading .......",
            reply_to_message_id=update.message_id
        )
        file_path = await bot.download_media(
            message=update.reply_to_message,
            file_name=DOWNLOAD_DIR + "/"
        )
        await bot.edit_message_text(
            chat_id=update.chat.id,
            message_id=init_msg.message.id,
            text="Scanning........Uwu........"
        )
        msg, video_link = await tracemoe_trace(file_path)
        await bot.edit_message_text(
            chat_id=update.chat.id,
            message_id=init_msg.message.id,
            text=msg
        )
        if video_link:
            await bot.send_video(
                chat_id=update.chat.id,
                video=video_link,
                reply_to_message_id=update.message.id
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="Reply to trace",
            reply_to_message_id=update.message.id
        ) 


