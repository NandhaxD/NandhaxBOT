

import io

from Katsuki import session 

#make a carbon image ( input text )
async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = io.BytesIO(await resp.read())
    image.name = "carbon.png"
    return image



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
                  
