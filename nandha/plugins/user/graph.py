from telegraph import upload_file, Telegraph
from pyrogram import filters
from nandha import app, lang
import config, os





""" MEDIA UPLOADER """

@app.on_message(filters.command("tm", prefixes=config.PREFIXES) & filters.me)
async def tm(_, message):
    await message.edit(lang['alyz'])
    reply_is = message.reply_to_message
    if not reply_is:
         return await message.edit_text(lang['reply_to_media'])
    types = [True if reply_is.document else True if reply_is.photo else True if reply_is.animation else False][0]
    if types:
        path = await message.reply_to_message.download()
        grap = upload_file(path)
        for code in grap:
              url = "https://graph.org"+code
        return await message.edit(str(url))



""" PAGE CREATOR """

telegraph = Telegraph()
telegraph.create_account(short_name=config.NAME)


@app.on_message(filters.command("txt", prefixes=config.PREFIXES))
async def graph_text(_, message):
     
     if message.from_user:
          first_name = message.from_user.first_name
     else:
          first_name = config.NAME
     if len(message.text.split()) >= 2:
           text = message.text.split(maxsplit=1)[1]
     else:
              if message.reply_to_message and (message.reply_to_message.document and bool(message.reply_to_message.document.mime_type.startswith("text/"))): 
                  path = await app.download_media(message.reply_to_message)
                  file = open(path, "r") 
                  text = file.read() 
                  file.close() 
                  os.remove(path)
              elif message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
                    text = (message.reply_to_message.text or message.reply_to_message.caption)
              else:
                  return await message.edit(lang['reply_to'])
     response = telegraph.create_page(first_name, html_content=text)
     page_url = response['url']
     return await message.edit(page_url)
