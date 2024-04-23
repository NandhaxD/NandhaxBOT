

"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





import requests 
import datetime 
import pytz
import re, io
import time

from telegraph import upload_file
from nandha import aiohttpsession


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = io.BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

async def get_note_deatils(msg):
     reply = msg.reply_to_message
     text = None
     file_id = None
     caption = None
     type = None
     if msg.text and not reply:
        note_name = msg.text.split()[1]
        text = msg.text.split(None, 2)[2]
        type = "#TEXT"
     elif reply:
           note_name = msg.text.split()[1]
           if reply.text:
               text = reply.text
               type = "#TEXT"
           elif reply.sticker:
               file_id = reply.sticker.file_id
               type = "#STICKER"
           elif reply.photo:
               file_id = reply.photo.file_id
               type = "#PHOTO"
               if reply.caption:
                   caption = reply.caption               
           elif reply.video:
               file_id = reply.video.file_id
               type = "#VIDEO"
               if reply.caption:
                   caption = reply.caption                 
           elif reply.document:            
               file_id = reply.document.file_id
               type = "#DOCUMENT"
               if reply.caption:
                   caption = reply.caption
     return text, file_id, type, caption


async def post(url: str, *args, **kwargs):
    async with aiohttpsession.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

async def get(url: str, *args, **kwargs):
    async with aiohttpsession.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data



async def match_text(pattern, text):
    regex = re.compile(pattern, re.IGNORECASE)
    return bool(regex.match(text))
     


async def emoji_convert(query):
     if query==True:
         return "✅"
     elif query==False:
         return "❌"
     elif query==None:
         return "🤷"
     else:
          return "🤔"



async def progress(c, t, msg, text, start):
         now = time.time()
         diff = now - start
         if round(diff % 10.00) == 0 or c == t:
               await msg.edit(f"**{text}... {c*100/t:.1f} %**")



async def grap(path):
     try:
         grap = upload_file(path)
         for id in grap:
              url = f"https://graph.org{id}"
     except:
          return False
     return url


anime_gif_key = ["lurk", "shoot", "sleep", "shrug", "stare", "wave", "poke", "smile", "peck",
           "wink", "blush", "smug", "tickle", "yeet", "think", "highfive", "feed",
           "bite", "bored", "nom", "yawn", "facepalm", "cuddle", "kick", "happy",
           "hug", "baka", "pat", "nod", "nope", "kiss", "dance", "punch", "handshake",
           "slap", "cry", "pout", "handhold", "thumbsup", "laugh"]



async def get_anime_gif(key):
    data = requests.get(f"https://nekos.best/api/v2/{key}").json()
    img = data['results'][0]["url"]
    return img
    


async def railway_to_normal(time_str):
    hour = int(time_str[:2])
    minute = time_str[3:5]
    suffix = "AM" if hour < 12 else "PM"
    hour = hour % 12 if hour != 12 else hour
    return "{}:{} {}".format(hour, minute, suffix)



async def get_datetime():
    timezone = pytz.timezone("Asia/Kolkata")
    kkk = str(datetime.datetime.now(timezone))
    TIME = kkk.split()[1]
    date = kkk.split()[0]
    time = await railway_to_normal(TIME)
    return {"date": date, "time": time}




async def convert_to_datetime(timestamp): # Unix timestamp
     date = datetime.datetime.fromtimestamp(timestamp)
     return date


async def batbin(text: str):
    url = "https://batbin.me/api/v2/paste"
    req = await post(url, data=text)
    if req['success']:
         return url.split('api')[0]+req['message']
    return False
    
async def spacebin(text: str):
    url = "https://spaceb.in/api/v1/documents/"
    response = requests.post(url, data={"content": text, "extension": "txt"})
    id = response.json().get('payload').get('id')
    res = requests.get(f"https://spaceb.in/api/v1/documents/{id}").json()
    created_at = res.get("payload").get("created_at")
    link = f"https://spaceb.in/{id}"
    raw = f"https://spaceb.in/api/v1/documents/{id}/raw"
    dict = {"result": {"link": link, "raw": raw, "datetime": created_at}}
    return dict 


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["seconds", "minutes", "hours", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
                  
