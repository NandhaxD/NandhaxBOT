from pyrogram import filters 
from Katsuki import apl
from requests import get

import os
import config

@app.on_message(filters.me & filters.command("git",prefixes=config.HANDLER))
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("where you input the username?\n")
    user = message.text.split(None, 1)[1]
    res = get(f'https://api.github.com/users/{user}').json()
    data = f"""**Name**: {res['name']}
**UserName**: {res['login']}
**Link**: [{res['login']}]({res['html_url']})
**Bio**: {res['bio']}
**Company**: {res['company']}
**Blog**: {res['blog']}
**Location**: {res['location']}
**Public Repos**: {res['public_repos']}
**Followers**: {res['followers']}
**Following**: {res['following']}
**Acc Created**: {res['created_at']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res['avatar_url']).content
        f.write(kek)

    await message.reply_photo(f"{user}.jpg", caption=data, quote=True)
    os.remove(f"{user}.jpg")
    await message.delete()
    return 
