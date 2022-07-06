import os
import wget
import random

from pyrogram import Client, filters
from pyrogram.types import *

from PIL import Image, ImageDraw, ImageFont
from Katsuki import katsuki
import config


async def edit_or_reply(message, text):
    """Edit Message If Its From Self, Else Reply To Message, (Only Works For Sudo's)"""
    if not message:
        return await message.edit(text)
    if not message.from_user:
        return await message.edit(text)
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message.id
            return await message.reply_text(
                text, reply_to_message_id=kk
            )
        return await message.reply_text(text)
    return await message.edit(text)

def choose_random_font():
    fonts_ = [
        "https://github.com/DevsExpo/FONTS/raw/main/Ailerons-Typeface.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/Toxico.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/againts.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/go3v2.ttf",
        "https://github.com/DevsExpo/FONTS/raw/main/vermin_vibes.ttf",
    ]
    random_s = random.choice(fonts_)
    return wget.download(random_s)

def get_text(message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@katsuki.on_message(filters.command("logo",prefixes=config.HANDLER) & filters.me)
async def logo(_, message):
    event = await edit_or_reply(message, "`Processing.....`")
    text = get_text(message)
    if not text:
        await event.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    font_ = choose_random_font()
    img = Image.open("./Katsuki/katsuki_help/IMG_20220701_185623_542.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, 220)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    draw.text(
        ((image_widthz - w) / 2, (image_heightz - h) / 2),
        text,
        font=font,
        fill=(random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)),
    )
    file_name = "LogoBy@KatsukiBoy.png"
    img.save(file_name, "png")
    if message.reply_to_message:
        await katsuki.send_photo(
            message.chat.id,
            photo=file_name,
            caption="Made by Katsuki",
            reply_to_message_id=message.reply_to_message.message.id,
        )
    else:
        await katsuki.send_photo(
            message.chat.id, photo=file_name, caption="Made by Katsuki"
        )
    await event.delete()
    if os.path.exists(file_name):
        os.remove(file_name)

