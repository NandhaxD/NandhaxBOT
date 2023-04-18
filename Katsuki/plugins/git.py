from pyrogram import filters 
from Katsuki import katsuki 
from requests import get

import os
import config

@katsuki.on_message(filters.user(config.OWNER_ID) & filters.command("git",prefixes=config.HANDLER))
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Enter GitHub Username To Find!\n")
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

    await message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
     
