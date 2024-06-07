


import requests
import config

from pyrogram import filters, types, enums, errors
from nandha import bot
from nandha.helpers.help_func import generate_random_code



url = "https://api.github.com/gists"


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
    "X-GitHub-Api-Version": "2022-11-28"
}



@bot.on_message(filters.command("gists") & filters.user(config.OWNER_ID))
async def gists_paste(bot, message):
     reply = message.reply_to_message
     name = message.from_user.first_name
     
     if reply and (reply.text or (reply.document and reply.document.mime_type.split('/')[0] == 'text')):
         if reply.document:
             file = await reply.download()
             with open(file, 'r') as f:
                 text = f.read()
             file_name = reply.document.file_name
         else:
              text = reply.text
              file_name = generate_random_code() + '.py'
         data = {
    "description": f"Code posted by {name}",
    "public": True,
    "files": {
        file_name: {
            "content": text
        }
    }
         }
         
         response = requests.post(url, headers=headers, json=data)
         if response.status_code == 201:
              data = response.json()
              url = data['html_url']
              return await message.reply_text(url)
         else:
            return await message.reply_text(f"❌ Something went wrong status code: {response.status_code}")
     else:
       return await message.reply_text("`Reply to the message text or a text document file`")




