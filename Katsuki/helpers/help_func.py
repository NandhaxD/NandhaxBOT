
import requests 
import datetime 

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
    timedate = await convert_to_datetime(created_at)
    string = f"""\n
**Paste link**: **[Paste link]({link})**
**Paste Raw link**: **[Raw View]({raw})**
**Created at**: {timedate}
"""
    return string


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
                  
