

"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





import requests 
import datetime 
import pytz
import re



async def emoji_convert(query):
     if query==True:
         return "✅"
     elif query==False:
         return "❌"
     elif query==None:
         return "🤷"
     else:
          return "🤔"


async def pypi_search(query):
    results = []
    content = requests.get(f"https://pypi.org/search/?q={query}").content.decode('utf-8')
    pattern_title = r'<span class="package-snippet__name">(.+?)<\/span>'
    pattern_version = r'<span class="package-snippet__version">(.+?)<\/span>'
    pattern_created = r'<time datetime="(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4})".*?>'
    pattern_description = r'<p class="package-snippet__description">(.+?)<\/p>?'
    package_snippets = re.findall(r'<a class="package-snippet".*?>(.*?)<\/a>', content, re.DOTALL)
    for snippet in package_snippets:
        try:
            title = re.search(pattern_title, snippet).group(1)
        except AttributeError:
            title = None
        try:
            version = re.search(pattern_version, snippet).group(1)
        except AttributeError:
            version = None
        try:
            created = re.search(pattern_created, snippet).group(1)
            created = created.replace('T', ' ').replace('+0000', '')
        except AttributeError:
            created = None
        try:
            description = re.search(pattern_description, snippet).group(1)
        except AttributeError:
            description = None
        data = {"title": title, "version": version, "created": created, "description": description}
        results.append(data)
    return results



async def FileType(message):
    if message.document:
        type = message.document.mime_type
        return ["txt" if type == "text/plain" else type.split("/")[1]][0]
    elif message.photo:
          return "jpg"
    elif message.animation:
          return message.animation.mime_type.split("/")[1]
    elif message.video:
         return message.video.mime_type.split("/")[1]
    else:
         return False


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
                  
