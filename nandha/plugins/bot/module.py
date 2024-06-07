

from nandha import bot, lang
from nandha.helpers.help_func import get as async_get
from nandha.helpers.function import extract_user, get_file_id 
from urllib.parse import quote
from pyrogram import filters, enums
from bs4 import BeautifulSoup
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegraph.aio import Telegraph
from typing import Union

from pyrogram.errors import (
    ChatAdminRequired,
    MessageTooLong,
    QueryIdInvalid,
    UserNotParticipant,
)

import pyrogram
import speedtest
import json
import contextlib
import os
import sys
import html
import traceback
import requests as fetch

def convert(speed):
    return round(int(speed) / 1_000_000, 3)
	
@bot.on_message(filters.command("speedtest"))
async def speedtest_func(client, message):
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    speedtest_image = speed.results.share()

    result = speed.results.dict()
    msg = (
    f"**Download**: {convert(result['download'])}Mb/s"
    f"\n**Upload**: {convert(result['upload'])}Mb/s"
    f"\n**Ping**: {result['ping']}"
    )
    await message.reply_photo(speedtest_image, caption=msg)



@bot.on_message(filters.command(['bard','gpt', 'palm']))
async def artificial_intelligent(_, message):

	reply = message.reply_to_message
	
	if len(message.command) <2:
		return await message.reply(lang['query'])

	reply_func = reply.reply_text if reply else message.reply_text
	reply = await reply_func(lang['thinking'])
	model = message.command[0]
	prompt = message.text.split(None, 1)[1]
	api = f"https://nandha-api.onrender.com/ai/{model}/{quote(prompt)}"	
	try:		
	    response = await async_get(api)
	    ok = response.get('content')		
	except Exception as e:
		 return await reply.edit(lang['error'].format(str(e)), parse_mode=enums.ParseMode.HTML)				
	return await reply.edit(lang['AI'].format(model.upper(), prompt, ok), parse_mode=enums.ParseMode.HTML)




@bot.on_message(filters.command("readqr"))
async def readqr(c, m):
    if not m.reply_to_message:
        return await m.reply("Please reply with a photo that contains a valid QR Code.")
    if not m.reply_to_message.photo:
        return await m.reply("Please reply with a photo that contains a valid QR Code.")
    
    # Download the photo
    foto = await m.reply_to_message.download()
    
    # Prepare the file for upload
    with open(foto, "rb") as f:
        files = {"file": f}
        url = "http://api.qrserver.com/v1/read-qr-code/"
        
        # Post the request
        r = requests.post(url, files=files)
    
    # Remove the downloaded photo
    os.remove(foto)
    
    # Check the response
    response = r.json()
    data = response[0]["symbol"][0]["data"]
    if data is None:
        return await m.reply_text("Could not read the QR code.")
    
    await m.reply_text(
        f"<b>QR Code Reader by @{c.me.username}:</b> <code>{data}</code>",
        quote=True,
    )


@bot.on_message(filters.command("createqr"))
async def makeqr(c, m):
    if m.reply_to_message and m.reply_to_message.text:
        teks = m.reply_to_message.text
    elif len(m.command) > 1:
        teks = m.text.split(None, 1)[1]
    else:
        return await m.reply(
            "Please add text after command to convert text -> QR Code."
        )
    url = f"https://api.qrserver.com/v1/create-qr-code/?data={quote(teks)}&size=300x300"
    await m.reply_photo(
        url, caption=f"<b>QR Code Maker by @{c.me.username}</b>", quote=True
    )


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re

    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)
  
@bot.on_message(filters.command(["sof"]))
async def stackoverflow(_, message):
    if len(message.command) == 1:
        return await message.reply("Give a query to search in StackOverflow!")
    r = (
        fetch.get(
            f"https://api.stackexchange.com/2.3/search/excerpts?order=asc&sort=relevance&q={message.command[1]}&accepted=True&migrated=False¬ice=False&wiki=False&site=stackoverflow"
        )
    ).json()
    msg = await message.reply("Getting data..")
    hasil = ""
    for count, data in enumerate(r["items"], start=1):
        question = data["question_id"]
        title = data["title"]
        snippet = (
            remove_html_tags(data["excerpt"])[:80].replace("\n", "").replace("    ", "")
            if len(remove_html_tags(data["excerpt"])) > 80
            else remove_html_tags(data["excerpt"]).replace("\n", "").replace("    ", "")
        )
        hasil += f"{count}. <a href='https://stackoverflow.com/questions/{question}'>{title}</a>\n<code>{snippet}</code>\n"
    try:
        await msg.edit(hasil)
    except MessageTooLong:
        path = f"{message.from_user.id}_sof.txt"
        with open(path, 'w') as f:
            f.write(hasil)
        await msg.reply_document(document=path)
    except Exception as e:
        await msg.edit(e)





@bot.on_message(filters.command(["id"]))
async def showid(_, message):
    chat_type = message.chat.type.value
    if chat_type == 'private':
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>➲ First Name:</b> {first}\n<b>➲ Last Name:</b> {last}\n<b>➲ Username:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True,
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>➲ Chat ID</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>➲ Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id, quote=True)




@bot.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    if message.sender_chat:
        return await message.reply_text(
          "Not supported channel.."
        )
    status_message = await message.reply_text("`Fetching user info...`")
    await status_message.edit(
      "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        return await status_message.edit(str(error))
    if from_user is None:
        return await status_message.edit(
          "No valid user_id / message specified"
        )
    message_out_str = ""
    username = f"@{from_user.username}" or "<b>No Username</b>"
    dc_id = from_user.dc_id or "<i>[User Doesn't Have Profile Pic]</i>"
    bio = (await client.get_chat(from_user.id)).bio
    count_pic = await client.get_chat_photos_count(from_user.id)
    message_out_str += f"<b>🔸 First Name:</b> {from_user.first_name}\n"
    if last_name := from_user.last_name:
        message_out_str += f"<b>🔹 Last Name:</b> {last_name}\n"
    message_out_str += f"<b>🆔 User ID:</b> <code>{from_user.id}</code>\n"
    message_out_str += f"<b>✴️ User Name:</b> {username}\n"
    message_out_str += f"<b>💠 Data Centre:</b> <code>{dc_id}</code>\n"
    if bio:
        message_out_str += f"<b>👨🏿‍💻 Bio:</b> <code>{bio}</code>\n"
    message_out_str += f"<b>📸 Pictures:</b> {count_pic}\n"
    message_out_str += f"<b>🧐 Restricted:</b> {from_user.is_restricted}\n"
    message_out_str += f"<b>✅ Verified:</b> {from_user.is_verified}\n"
    message_out_str += f"<b>🌐 Profile Link:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type.value in (("supergroup", "channel")):
        with contextlib.suppress(UserNotParticipant, ChatAdminRequired):
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = chat_member_p.joined_date
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>" f"{joined_date}" "</code>\n"
            )
    if chat_photo := from_user.photo:
        local_user_photo = await client.download_media(message=chat_photo.big_file_id)
        buttons = [
            [
                InlineKeyboardButton(
                    "🔐 Close", callback_data=f"close#{message.from_user.id}"
                )
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            disable_notification=True,
        )
        os.remove(local_user_photo)
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "🔐 Close", callback_data=f"close#{message.from_user.id}"
                )
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            disable_notification=True,
        )
    await status_message.delete()


@bot.on_callback_query(filters.regex("^close"))
async def close_callback(_, query: CallbackQuery):
    _, userid = query.data.split("#")
    if query.from_user.id != int(userid):
        with contextlib.suppress(QueryIdInvalid):
            return await query.answer("⚠️ Access Denied!", True)
    with contextlib.redirect_stdout(Exception):
        await query.answer("Deleting this message in 5 seconds.")
        await asyncio.sleep(5)
        await query.message.delete()
        await query.message.reply_to_message.delete()



@bot.on_message(filters.command(["ocr"]))
async def ocr(_, ctx: Message):
    reply = ctx.reply_to_message
    if (
        not reply
        or not reply.sticker
        and not reply.photo
        and (not reply.document or not reply.document.mime_type.startswith("image"))
    ):
        return await ctx.reply_text(
            "Reply to the media", quote=True
        )
    msg = await ctx.reply_text("Reading the media...", quote=True)
    try:
        file_path = await reply.download()
        if reply.sticker:
            file_path = await reply.download(
                f"ocr_{ctx.from_user.id if ctx.from_user else ctx.sender_chat.id}.jpg"
            )
        response = await Telegraph().upload_file(file_path)
        url = f"https://img.yasirweb.eu.org{response[0]['src']}"
        req = fetch.get(
                f"https://script.google.com/macros/s/AKfycbwURISN0wjazeJTMHTPAtxkrZTWTpsWIef5kxqVGoXqnrzdLdIQIfLO7jsR5OQ5GO16/exec?url={url}"
                 ).json()
        await msg.edit_text(req["text"])
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        await msg.edit_text(str(e))
        if os.path.exists(file_path):
            os.remove(file_path)

