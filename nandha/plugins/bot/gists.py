


import requests
import config

from pyrogram import filters, types, enums, errors
from nandha import bot
from nandha.helpers.help_func import generate_random_code


GITHUB_USERNAME = "NandhaXD"
API_URL = "https://api.github.com/gists"
PROFILE_LINK = "https://github.com/{}"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
    "X-GitHub-Api-Version": "2022-11-28"
}



@bot.on_message(filters.command("delgist") & filters.user(config.OWNER_ID))
async def DeleteGist(bot, message):

      if len(message.text.split()) == 1:
          return await message.reply_text("Where is that unique gist ID?```Example:\n/delgist git id```")
      msg = await message.reply_text("Deleting....")
      gist_id = message.text.split()[1]
      url = f"https://api.github.com/gists/{gist_id}"
      response = requests.delete(url, headers=headers)
      if response.status_code == 204:
           return await msg.edit("✅ Successfully deleted the Gist")
      else:
           return await msg.edit_text(f"❌ Something went wrong status code: {response.status_code}")
        
      
@bot.on_message(filters.command("gistlist") & filters.user(config.OWNER_ID))
async def GistList(bot, message):
       msg = await message.reply_text("Getting gists list....")

       if len(message.text.split()) == 2:
             GITHUB_USERNAME = message.text.split()[1]
             
       response = requests.get(f'https://api.github.com/users/{GITHUB_USERNAME}/gists').json()
       text = f"**✨ [{GITHUB_USERNAME}]({PROFILE_LINK.format(GITHUB_USERNAME)}) List of Gists**:\n\n"
       if response.status_code != 200:
            return await msg.edit("Validation failed, or the endpoint has been spammed, or not found")
       if not response:
           return awsit msg.edit("🤔 Seems like nothing in that user gist")
       for idx, gist in enumerate(response, start=1):
           for file_name in gist['files'].keys():
               text += f"{idx}. [{file_name}]({gist['html_url']}), `{gist['id']}`\n"
       await msg.edit(text)
                

@bot.on_message(filters.command("gist") & filters.user(config.OWNER_ID))
async def GistPaste(bot, message):
     reply = message.reply_to_message
     name = message.from_user.first_name

     msg = await message.reply_text("⏳ Pasting In Gist.....")
     if reply and (reply.text or (reply.document and reply.document.mime_type.split('/')[0] == 'text')):
         if reply.document:
             await msg.edit("Downloading the file.....")
             file = await reply.download()
             with open(file, 'r') as f:
                 text = f.read()
             file_name = reply.document.file_name
         else:
              if len(message.text.split()) == 1:
                    return await msg.edit_text(
                      "Can you please provide the extension for the file? Eg: py, txt, js ect..."
                    )
              extension = message.text.split()[1]
              text = reply.text
              file_name = generate_random_code() + '.' + extension if not '.' in extension else extension.split('.')[1]
         data = {
    "description": f"Code posted by {name}",
    "public": True,
    "files": {
        file_name: {
            "content": text
        }
    }
         }
         
         response = requests.post(API_URL, headers=headers, json=data)
         if response.status_code == 201:
              data = response.json()
              url = data['html_url']
              return await msg.edit_text(url)
         else:
            return await msg.edit_text(f"❌ Something went wrong status code: {response.status_code}")
     else:
       return await msg.edit_text("`Reply to the message text or a text document file`")




